import re
from methods import word_presence_checker, number_extraction_from_text, extract_order_and_warehouse, clean_messy_text, validate_email_format


proceed='y'
while proceed.lower()=='y':
    print("\n\033[105mSelect a task to perform:\033[0m\n")
    print("\033[4;37m1. Word Presence Checker\033[0m")
    print("\033[4;37m2. Number Extraction from Text\033[0m")
    print("\033[4;37m3. Order and Warehouse Extraction\033[0m")
    print("\033[4;37m4. Clean Messy Text\033[0m")
    print("\033[4;37m5. Basic Email Format Validation\033[0m")
    
    choice = input("\n\033[106;4mEnter the task number (1-5): \033[0m")
    
    if choice == '1':
        sentence = input("\033[43;30;1mEnter a sentence: \033[0m")
        target_word = input("\033[43mEnter the target word: \033[0m")
        if word_presence_checker(sentence, target_word):
            print(f'\033[42mThe word "{target_word}" is present in the sentence.\033[0m')
        else:
            print(f'\033[41mThe word "{target_word}" is NOT present in the sentence.\033[0m')
    
    elif choice == '2': # special char chk trail  nd lead
        paragraph = input("\033[43mEnter a paragraph: \033[0m")
        extracted_numbers = number_extraction_from_text(paragraph)
        print(f"\033[42mExtracted numbers:{extracted_numbers}\033[0m")
    
    elif choice == '3':
        # input_text = input("\033[43mEnter the text containing order and warehouse info: \033[0m")
        input_text = "Order ID: AXT-2025 delivered to warehouse 18"
        order_code, warehouse_number = extract_order_and_warehouse(input_text)
        print("Order Code:", order_code)
        print("Warehouse Number:", warehouse_number)
    
    elif choice == '4':
        messy_text = input("\033[43mEnter messy text to clean: \033[0m")
        cleaned_text = clean_messy_text(messy_text)
        print("Cleaned Text:", cleaned_text)
    
    elif choice == '5':
        email_input = input("\033[43mEnter an email address to validate: \033[0m")
        validation_result = validate_email_format(email_input)
        print(validation_result)
    
    else:
        print("\033[41mInvalid choice. Please select a valid task number.\033[0m")
    
    proceed = input("\n\033[43mDo you want to perform another task? (y/n): \033[0m")
print("\033[42mThank you for using the program. Goodbye!\033[0m")