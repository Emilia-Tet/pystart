# zadanie 1 - match case
# dla uzytkownika dac 4 podstawowe operacje matematyczne na 2 wybranych liczbach

# zadanie 2
# konwersja kilogramy - funty - uncje 1 kg = 35.274 uncji, 1 kg = 2.20462

# zadanie 3
# zdefiniuj haslo w zmiennej i petle while ktora bedzie pytac o wprowadzenie hasla. 
# wyswietl albo "poprawne haslo" albo "niepoprawne, sprobuj jeszcze raz"

# zadanie 4
# program symulujacy dzialanie bankomatu, petla while prosi o wybor operacji " wplata, wyplata, stan konta, wyjscie"
# pyta dopoki nie wybierze wyjscie

# zadanie 5
# program pyta o miasto i temperature w Celsj. przechowuje wartosci w slowniku.
# dopoki uzytkownik nie wprowadzi "koniec"
# wtedy ywswietla srednia temperature dla wszystkich miast i nazwe miast z najniznsza i najwyzasza temp

# zadanie 7 
# program pyta o wprowadzanie iiczb dopoki nie wprowadzi 0. jesli parzyste, dodaje do listy 
# i parzyste tez. Na koniec wyswieta liczbe parz i nieparz oraz listy liczb

even_num = []
odd_num = []

while (users_input := int(input("Podaj liczbe calkowita lub 0 by zakonczyc: "))) >0:
    if users_input %2 == 0:
        even_num.append(users_input)
    else:
        odd_num.append(users_input)

print(f"Ilosc nieparzystych liczb: {len(odd_num)}. "
      f"Ilosc parzystych liczb: {len(even_num)}.")

print("Zebrane liczby nieparzyste: ")
print(*odd_num, sep=',')
print("\n")

print("Zebrane liczby parzyste: ")
for num in even_num:
    print(str(num), end = ' ')

#Here a single asterisk( * ) is also used in *args. It  is used to pass a variable number of arguments to a function, it is mostly used to pass a non-key argument and variable-length argument list.
#It has many uses, one such example is illustrated below, we make an addition function that takes any number of arguments and able to add them all together using *args.

#cw 8 sklep
# slownik produkt - cena, zapytaj uzytkownika ktory produkt chce dodac i w jakiej ilosci
# pytaj uzytkownia co chce dodac dopoki nie wybierze podsumuj
# na koniec podsumowanie i cena koncowa

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
    order[cs_choice] = order.get(cs_choice+quantity, quantity)

print("Twoje zamowienie to: ")
for ind, item in enumerate(order):
    print(f"{ind+1}. {item} - {order[item]} szt.")
print(f"Wartosc zamowienia wynosi {sum(order.values())}")


    



    

