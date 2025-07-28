import random

def generate_card(bin_prefix):
    cc = bin_prefix + "".join([str(random.randint(0, 9)) for _ in range(16 - len(bin_prefix))])
    exp_month = f"{random.randint(1, 12):02d}"
    exp_year = str(random.randint(25, 29))
    cvv = str(random.randint(100, 999))
    return f"{cc}|{exp_month}|{exp_year}|{cvv}"
