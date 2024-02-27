import random

def get_numbers_ticket(min, max, quantity):
    
    result = set()
    if min < 1: 
        #print("first argument of the function is 'min' and must be > 0")
        return list(result)
    if max < min:
        #print("second argument of the function is 'max' and must be bigger than the first argument 'min'")
        return list(result)
    if max > 1000:
        #print("second argument of the function is 'max' and must be <= 1000")
        return list(result)
    if quantity > max-min+1 or quantity <= 0:
        #print("third argument of the function is 'quantity' and must be 0 < quantity <= max-min+1 ")
        return list(result)

    while len(result) < quantity:
        result.add(random.randint(min, max))
    result_list = list(result)
    result_list.sort()
    return result_list

print(get_numbers_ticket(10,20,10))
#print (f"get_numbers_ticket returns {x}")