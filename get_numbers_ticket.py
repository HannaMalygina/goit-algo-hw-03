import random

def get_numbers_ticket(min, max, quantity):
    
    if min < 1: 
        #print("first argument of the function is 'min' and must be > 0")
        return ""
    if max < min:
        #print("second argument of the function is 'max' and must be bigger than the first argument 'min'")
        return ""
    if max > 1000:
        #print("second argument of the function is 'max' and must be <= 1000")
        return ""
    if quantity > max-min+1 or quantity <= 0:
        #print("third argument of the function is 'quantity' and must be 0 < quantity <= max-min+1 ")
        return ""

    result = set()
    while len(result) < quantity:
        result.add(random.randint(min, max))
    result_list = list(result)
    result_list.sort()
    return result

get_numbers_ticket(10,20,12)
#print (f"get_numbers_ticket returns {x}")