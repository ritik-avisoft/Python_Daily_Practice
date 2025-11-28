import re
def word_presence_checker(sentence, target_word):
    pattern = r'\b' + re.escape(target_word) + r'\b' # Pattern to match the target word as a standalone word
    if re.search(pattern, sentence, re.IGNORECASE):
        return True
    else:
        return False
    
def number_extraction_from_text(paragraph):
    # pattern = r'\b-?\d+\b'  
    pattern = r'(?<!\w)-?\d+\b'  # Pattern to match standalone integers, including negative numbers
    numbers = re.findall(pattern, paragraph)
    return [int(num) for num in numbers]  # Convert extracted strings to integers

def extract_order_and_warehouse(text):
    order_pattern = r'\b([A-Za-z]+-\d+)\b'
    warehouse_pattern = r'\bwarehouse\s+(\d+)\b'
    
    order_match = re.search(order_pattern, text)
    warehouse_match = re.search(warehouse_pattern, text, re.IGNORECASE)
    
    order_code = order_match.group(1) if order_match else None
    warehouse_number = warehouse_match.group(1) if warehouse_match else None
    
    return order_code, warehouse_number

def clean_messy_text(messy_text):
    # Remove special characters except spaces and alphanumeric characters
    cleaned_text = re.sub(r'[^A-Za-z0-9\s]', '', messy_text)
    # Collapse multiple spaces into a single space
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    return cleaned_text.strip().lower()

def validate_email_format(email):
    pattern = r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if re.match(pattern, email):
        return "\033[42mValid email format\033[0m"
    else:
        return "\033[41mInvalid email format\033[0m"
    
