katalog = {'dlugopis' : 3,
         'olowek' : 2,
         'zeszyt' : 5,
         'kolonotatnik' : 8,
         'pioro' : 60}

print("Oto katalog sklepu Piorko:")
for index, i in enumerate(katalog):
    print(f"{index+1}. {i} : {katalog[i]} zl.")

order = {}

while (cs_choice:= input("Wpisz swoj wybor lub 'podsumuj' aby zakonczyc: ")) != 'podsumuj':
    quantity = int(input("Podaj ilosc: "))
    prev_quantity = order.get(cs_choice, 0)
    order[cs_choice] = prev_quantity + quantity
    # wersja Kacpra:
    # order[cs_choice] = order.get(cs_choice, 0) + int(input("Podaj ilosc: "))

final_order = 0
for ord in order:
    final_order+= katalog[ord]*order[ord]
# wersja Kacpra:
# for name, price in katalog.items():
# final_order += katalog[name]*quantity

print('---' * 10)
    
print("Twoje zamowienie to: ")
for ind, item in enumerate(order):
    print(f"{ind+1}. {item} - {order[item]} szt.")
print(f"Laczna ilosc zamowionych przedmiotow: {sum(order.values())}."
      f"Wartosc zamowienia wynosi {final_order} zl.")
if final_order < 120:
    print(f"Koszt przesylki wynosi 15 zl. Do darmowej przesylki brakuje Ci {120-final_order} zl.")
else:
    print("Przesylka bedzie darmowa!")