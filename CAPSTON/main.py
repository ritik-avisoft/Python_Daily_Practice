import json
import os
from datetime import datetime
from pathlib import Path

import cpmethods  # imported method file 


def main():
    # Load inventory at the start
    inventory = cpmethods.load_inventory_data(cpmethods.INVENTORY_FILE)

    while True:
        print("\n\033[1;107mInventory Management System\033[0m")
        print("\t1. View Current Inventory")
        print("\t2. Add New Product")
        print("\t3. Update Product Stock")
        print("\t4. Search Products")
        print("\t5. Generate Inventory Report")
        print("\t6. View Transaction History")
        print("\t7. Manually Backup Inventory Now")
        print("\t8. Start Backup Scheduler")
        print("\t9. Stop Backup Scheduler")
        print("\t10. Exit Program")

        choice = input("" \
        "\033[33mSelect an option (1-10): \033[0m").strip()


        # VIEW INVENTORY
        if choice == '1':
            cpmethods.display_inventory(inventory)

        # ADD NEW PRODUCT
        elif choice == '2':
            print("\n\033[1;33mEnter product details (type 'exit' to cancel):\033[0m")
            name = input("Product Name: ").strip()
            if cpmethods.check_exit(name):
                cpmethods.if_break()
                continue

            if not cpmethods.is_valid_string(name):
                print("Invalid product name.")
                continue

            category = input("Category: ").strip()
            if cpmethods.check_exit(category):
                continue

            try:
                price = float(input("Price: ").strip())
                quantity = int(input("Initial Quantity: ").strip())
            except ValueError:
                print("Price and Quantity must be numeric.")
                continue

            try:
                inventory, product_id = cpmethods.add_new_product(
                    inventory, name, category, price, quantity
                )
                cpmethods.log_transaction("NEW_ITEM", product_id, quantity)
                print(f"\033[32mProduct added successfully with ID: {product_id}\0330m")
            except ValueError as e:
                print("Error:", e)

        # UPDATE STOCK
        elif choice == '3':
            product_id = input("\033[33mEnter Product ID: \033[0m").strip()

            if product_id not in inventory:
                print("\033[31mProduct not found.\033[0m")
                continue

            try:
                qty_change = int(input("\033[33mEnter quantity change (+ for adding/- for removing product quantity): \033[0m"))
                inventory = cpmethods.update_product_quantity(inventory, product_id, qty_change)
                cpmethods.log_transaction(
                    "STOCK_ADD" if qty_change > 0 else "STOCK_REMOVE",
                    product_id,
                    qty_change
                )
                print(f"\033[32mStock updated successfully for product {product_id}.\033[0m")
            except ValueError as e:
                print("Error:", e)

        # SEARCH PRODUCTS
        elif choice == '4':
            term = input("\033[33mEnter name/category to search: \033[0m").strip()
            results = cpmethods.search_products(inventory, term)
            cpmethods.display_inventory(results)

        # INVENTORY REPORT
        elif choice == '5':
            report = cpmethods.generate_inventory_report(inventory)
            print("\n\033[1;92;107mInventory Report\033[0m")
            for key, value in report.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

        # VIEW LOG HISTORY
        elif choice == '6':
            print("\n\033[1;92;107mTransaction History \033[0m")
            if os.path.exists(cpmethods.TRANSACTION_LOG_FILE):
                with open(cpmethods.TRANSACTION_LOG_FILE, 'r') as file:
                    print(file.read())
            else:
                print("\033[91mNo transaction history found.\033[0m")

        # BACKUP NOW
        elif choice == '7':
            cpmethods.backup_inventory_data(cpmethods.INVENTORY_FILE)
            print("\033[92mBackup completed.\033[0m")

        # START SCHEDULER
        elif choice == '8':
            cpmethods.start_scheduler()

        # STOP SCHEDULER
        elif choice == '9':
            cpmethods.stop_scheduler_thread()

        # EXIT
        elif choice == '10':
            print("Saving inventory and exiting program...")
            cpmethods.save_inventory_data(cpmethods.INVENTORY_FILE, inventory)
            print("\033[92m Auto Stopping the Auto Scheduler. \033[0m")
            # cpmethods.stop_scheduler_thread()
            break

        # INVALID INPUT
        else:
            print("Invalid choice. Please choose between 1–10.")


if __name__ == "__main__":
    main()
