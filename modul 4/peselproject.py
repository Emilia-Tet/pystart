# sprawdzic czy ma 11 cyfr
# przemnozony przez liczbe kontrolna, ostatnia liczba to musi byc 0
# liczba kontrolna to: 13791379131 i mnozymy po kolei pierwsza cyfre przez 1, druga przez 3 itd
# na koniec dodajemy te wartosci, jesli na koncu jest 0 to pasuje

pesel_list = list(input("Podaj swoj pesel: "))
control_num = list(str(13791379131))

if len(pesel_list) == 11:
    print(f"Twoj PESEL ma {len(pesel_list)} cyfr zamiast 11.")
    quit()

sum = 0
for pnum, connum in zip(pesel_list, control_num):
    sum += (int(pnum)*int(connum))

if sum%10 ==0:
    print("Twoj PESEL jest poprawny.")
else:
    print("Twoj pesel nie jest poprawny!")

