import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1: 
        print("first argument of the function is 'min' and must be > 0")
        return ""
    if max < min:
        print("second argument of the function is 'max' and must be bigger than the first argument 'min'")
        return ""
    if max > 1000:
        print("second argument of the function is 'max' and must be <= 1000")
        return ""
    if quantity > max or quantity < min:
        print("third argument of the function is 'quantity' and must be min < quantity < max ")
        return ""

    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))
    result_list = list(result)
    result_list.sort()
    return result

