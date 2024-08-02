def calculate_brutto(amount, tax=0.23):
    return amount*(1+tax)

def calculate_netto(amount, tax=0.23):
    return amount/(1+tax)

def calculate_discount(total: float, discounts: list)-> float:
    for discount in discounts:
        total -= total * discount
    return total