import re

def normalize_phone(phone_number):
    phone_number_init = phone_number
    pattern_remove_symbols = r"\D+"
    replacement = ""
    phone_number_wo_symbols = re.sub(pattern_remove_symbols, replacement, phone_number_init)

    if phone_number_wo_symbols[0]=="3":
        phone_number_res = "+" + phone_number_wo_symbols
    else:
        phone_number_res = "+38" + phone_number_wo_symbols
    return phone_number_res
