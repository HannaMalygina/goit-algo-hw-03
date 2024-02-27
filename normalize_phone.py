import re

def normalize_phone(phone_number):
    phone_number_init = phone_number
    startsWithPlus = False
    if phone_number_init[0] == "+": startsWithPlus = True

    pattern_remove_symbols = r"\D+"
    replacement = ""
    phone_number_wo_symbols = re.sub(pattern_remove_symbols, replacement, phone_number_init)
    #print (f"{len(phone_number_wo_symbols)}")
    if startsWithPlus: 
        phone_number_res = "+" + phone_number_wo_symbols
    else:
        if len(phone_number_wo_symbols) > 10: 
            phone_number_res = "+" + phone_number_wo_symbols
        else:
            phone_number_res = "+38" + phone_number_wo_symbols
    return phone_number_res

print(normalize_phone("+49029375755"))
print(normalize_phone("4902935755"))