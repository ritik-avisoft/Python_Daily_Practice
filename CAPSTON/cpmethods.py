import json
import logging
import os
from datetime import datetime
from pathlib import Path
import re
import schedule
import threading
import time


BASE_DIR = Path(__file__).resolve().parent

INVENTORY_FILE = BASE_DIR / "inventory_data.json"
TRANSACTION_LOG_FILE = BASE_DIR / "transaction_log.txt"

#dir for backup 
BACKUP_DIR = Path(__file__).resolve().parent
BACKUP_DIR = BACKUP_DIR / "backups"

logging.basicConfig(
    filename=BASE_DIR / 'inventory_management.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#A method to check for quiting while entring data
def check_exit(value):
    if value.lower() in ("exit", "quit", "q", "back"):
        return True
    return False
#A method to validate input strings
def is_valid_string(value):
    if not isinstance(value, str):
        return False

    value = value.strip()
    if value == "":
        return False

    # Must start with a letter; allow letters, digits, spaces, hyphens
    pattern = r'^[A-Za-z][A-Za-z0-9 -]*$'
    return bool(re.fullmatch(pattern, value))
#Auto generating product id by incrementing 1 from the max(id)
def generate_product_id(inventory):
    if not inventory:
        return 1
    return max(int(pid) for pid in inventory.keys()) + 1
# A method to write log in txt
def log_transaction(action, product_id, quantity_change):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(TRANSACTION_LOG_FILE, 'a') as file:
        file.write(f"{timestamp} - ACTION: {action}, PRODUCT_ID: {product_id}, QUANTITY_CHANGE: {quantity_change}\n")
# Loading inventory Data
def load_inventory_data(file_path):
    if not os.path.exists(file_path):
        logging.info("No existing inventory found. Starting with empty inventory.")
        return {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            inventory = json.load(file)
    except json.JSONDecodeError:
        logging.exception("Inventory JSON corrupted. Starting with empty dict.")
        return {}
    return inventory
#Method to Dispplay all the data from inventory
def display_inventory(inventory):
    if not inventory:
        logging.info("Attempted to display empty inventory.")
        print("\033[31mInventory is empty.\033[0m")
        return

    print("\n\033[1;4;107mCurrent Inventory:\033[0m")
    print("{:<10} {:<20} {:<15} {:<10} {:<15}".format(
        'ID', 'Name', 'Category', 'Price', 'Quantity'
    ))

    for product_id, details in inventory.items():
        name = details.get('name', 'N/A')
        category = details.get('category', 'N/A')
        price = details.get('price', 0)
        quantity = details.get('quantity', 0)

        print("{:<10} {:<20} {:<15} {:<10} {:<15}".format(
            product_id,
            name,
            category,
            f"₹{price}",
            quantity
        ))
#Add new product in the inventory
def add_new_product(inventory, name, category, price, quantity):
    product_id = generate_product_id(inventory)  # auto ID
    # Vaidations for Valid parameters
    try:
        if price <= 0:
            logging.error("Attempted to add product with invalid price.")
            raise ValueError("\033[91mPrice must be greater than zero.\033[0m")

        if quantity < 0:  # allow zero quantity
            logging.error("Attempted to add product with negative quantity.")
            raise ValueError("\033[91mQuantity cannot be negative.\033[0m")

    except ValueError:
        logging.exception("033[91mError while adding new product data033[0m")
        raise
    # ADD PRODUCT
    new_product = {
        'name': name,
        'category': category,
        'price': price,
        'quantity': quantity,
        'last_restock_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    inventory[str(product_id)] = new_product

    # SAVE INVENTORY SAFELY
    try:
        save_inventory_data(INVENTORY_FILE, inventory)
    except Exception as e:
        logging.error(f"Save failed for product {product_id}. Rolling back.")
        del inventory[str(product_id)]  # rollback
        raise e

    logging.info(f"New product added successfully: {product_id} - {name}")
    return inventory, product_id

    

    # save to json immediately
    save_inventory_data(INVENTORY_FILE, inventory)
    logging.info(f"Added new product: {product_id} - {name}")
    return inventory, product_id
# To save the inventory data 
def save_inventory_data(file_path, inventory):
    try:
        with open(file_path, 'w') as file:
            json.dump(inventory, file, indent=4)
        logging.info("Inventory data saved successfully.")

    except Exception as e:
        logging.error(f"Failed to save inventory data: {e}")
        print(f"❌ Error: Could not save inventory data. {e}")

# To update product quantity
def update_product_quantity(inventory, product_id, quantity_change):
    if product_id not in inventory:
        logging.error(f"Attempted to update non-existent product ID: {product_id}")
        raise ValueError("033[91mProduct ID not found in inventory.033[0m")

    if quantity_change==0:
        logging.error(f"Invalid Quantity Update Operation for the product id {product_id}")
        raise ValueError("\033[91mInvalid Quantity to make any changes.\033[0m")
    
    new_quantity = inventory[product_id]['quantity'] + quantity_change
    if new_quantity < 0:
        logging.error(f"Insufficient stock for product ID: {product_id}")
        raise ValueError("033[91mInsufficient stock to remove the requested quantity.033[0m")

    inventory[product_id]['quantity'] = new_quantity
    if quantity_change > 0:
        inventory[product_id]['last_restock_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_inventory_data(INVENTORY_FILE, inventory)
    logging.info(f"Updated product ID {product_id} quantity by {quantity_change}. New quantity: {new_quantity}")
    return inventory
#search iteb by name or category
def search_products(inventory, search_term):
    results = {}
    for product_id, details in inventory.items():
        if (search_term.lower() in details['name'].lower() or
                search_term.lower() in details['category'].lower()):
            results[product_id] = details
    
    logging.info(f"Searched for products with term: {search_term}. Found {len(results)} results.")
    print( f"\n033[92mFound {len(results)} matching products for search term: '{search_term}'033[0m")
    return results
# For generating the report 
def generate_inventory_report(inventory):
    total_products = len(inventory)
    total_value = sum(details['price'] * details['quantity'] for details in inventory.values())
    low_stock_items = sum(1 for details in inventory.values() if details['quantity'] < 10) 
    if low_stock_items:
        logging.warning(f"Low stock items detected: {low_stock_items} items below threshold.")
    out_of_stock_items = sum(1 for details in inventory.values() if details['quantity'] == 0)
    if out_of_stock_items:
        logging.warning(f"Out of stock items detected: {out_of_stock_items} items are out of stock.")

    category_counts = {}
    for details in inventory.values():
        category = details['category']
        category_counts[category] = category_counts.get(category, 0) + details['quantity']

    most_stocked_category = max(category_counts, key=category_counts.get) if category_counts else None

    report = {
        'total_products': total_products,
        'total_value': total_value,
        'low_stock_items': low_stock_items,
        'out_of_stock_items': out_of_stock_items,
        'most_stocked_category': most_stocked_category
    }

    logging.info("Generated inventory report sucessfully.")
    return report
# add a weekly backup for the inventory json file data
def backup_inventory_data(INVENTORY_FILE):
    if not os.path.exists(INVENTORY_FILE):
        logging.error("Attempted to backup non-existent inventory file.")
        raise FileNotFoundError("033[91mInventory file not found for backup.033[0m")

    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)

    # generating a timestamped name for backup file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_path = BACKUP_DIR / f"inventory_backup_{timestamp}.json"

    with open(INVENTORY_FILE, 'r') as original_file:
        data = original_file.read()

    with open(backup_file_path, 'w') as backup_file:
        backup_file.write(data)

    logging.info(f"Inventory data backed up successfully to {backup_file_path}.")
    print(f"Inventory data backed up successfully as inventory_backup_{timestamp}.json.")
    return backup_file_path 

stop_scheduler = threading.Event()
scheduler_thread = None
def scheduled_backup():
    logging.info("Running scheduled backup...")
    backup_inventory_data(INVENTORY_FILE)

def run_scheduler():
    # REAL WEEKLY BACKUP (UNCOMMENT FOR FINAL VERSION)
    # schedule.every().sunday.at("11:00").do(scheduled_backup)

    # TEST MODE (runs every 5 seconds)
    schedule.every(5).seconds.do(scheduled_backup)
    while not stop_scheduler.is_set():
        schedule.run_pending()
        time.sleep(1)
# To start Auto Scheduler
def start_scheduler():
    global scheduler_thread
    stop_scheduler.clear()
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    print("\033[92mBackup scheduler started.\033[0m")
#To stope the auto Scheduler
def stop_scheduler_thread():
    stop_scheduler.set()
    print("\033[93mStopping scheduler...\033[0m")
    if scheduler_thread:
        scheduler_thread.join()
    print("\033[91mBackup scheduler stopped.033[0m")

def if_break():
    print("\n\033[1;101mProduct entry cancelled.\033[0m")
    print("Required fields were:")
    print("  • Product Name     → (letters/numbers, spaces allowed, must start with a letter)")
    print("  • Category         → (letters/numbers, spaces allowed, must start with a letter)")
    print("  • Price            → (positive number)")
    print("  • Quantity         → (positive integer)")
    print("\nYou exited before completing all required fields.\n")
    
