kwh_price = 0.617
time = 24
used_kwh = 10

# ctrl + shift + 2

def electricity_invoice(time:int, used_kwh:int, kwh_price = 0.617)-> int:
    
    '''This function counts the price of the electricity you have used.
    :param time: int, time of electricity running,
    :param used_kwh: int, used kilowathours,
    :param kwh_price: price of 1 kwh, basically 0.617'''
    return kwh_price*used_kwh/time

print(electricity_invoice(24, 10))

