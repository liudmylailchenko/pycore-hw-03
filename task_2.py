from random import randint

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except ValueError:
        return "Incorrect data format. Please enter numbers in format 'int'."
    
    if min < 1:
        return "The minimum number must be 1 or greater"
    
    if max > 1000:
        return "The maximum number must be 1000 or less."
    
    if min > max:
        return "The minimum number must be less than the maximum number."
    
    if quantity > max - min:
        return "The quantity of numbers must be less than the difference between the maximum and minimum numbers."
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(randint(min, max))
    
    return sorted(numbers)


