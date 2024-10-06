import re

def normalize_phone(phone_number: str) -> str:
    only_numbers = re.sub(r'\D+', '', phone_number)

    if (len(only_numbers) == 10):
        return '+38' + only_numbers
    elif (len(only_numbers) == 12): 
        return '+' + only_numbers
    else: 
        return 'Incorrect phone number format'