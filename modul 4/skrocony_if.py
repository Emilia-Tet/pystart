# schemat przypisywania zmiennej przy krotkich warunkach
value = 'value if true' if 1 == 1 else 'value if false'

ilosc_produktow = 2
rabat = 10 if ilosc_produktow > 3 else 0

result = 0.5
status = 'passed' if result >= 0.6 else 'failed'

# skrocony if cwiczenie
base = 5000
work_exp = 3
pieces_sold = 45
work_time = 168

prime1 = 0.02 if work_exp <=2 else 0.1
prime2 = 0.25 if pieces_sold > 30 else 0
prime_3 = 0.08 if work_time > 160 and work_exp > 1 else 0.02

payout = base + base*prime1 + base*prime2 + base*prime_3

# walrus
base = 5000
# work_exp = 3
# pieces_sold = 45
# work_time = 168

prime1 = 0.02 if (work_exp:= 3) <=2 else 0.1
prime2 = 0.25 if (pieces_sold:= int(input("Podaj ile sprzedales elementow "))) > 30 else 0
prime_3 = 0.08 if (work_time:= 168) > 160 and work_exp > 1 else 0.02

payout = base + base*prime1 + base*prime2 + base*prime_3
print(payout)