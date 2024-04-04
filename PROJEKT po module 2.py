ilosc_scian = int(input("Podaj ilość ścian do pomalowania: "))


szerokosci_suma = 0
wysokosci = []

while True:
    pytanie_wys = input("Czy wszystkie ściany mają taką samą wysokość? Odpowiedz tak lub nie.")
    if pytanie_wys.lower() == "tak":
        wysokosc_input = float(input("Podaj wysokosc sciany w metrach: "))

        for i in range(1, ilosc_scian+1):
                szerokosc = float(input(f"Podaj szerokość {i} ściany w metrach: "))
                szerokosci_suma+=szerokosc
        powierzchnia_sum = szerokosci_suma*wysokosc_input
        print(f"Powierzchnia ścian do pomalowania wynosi {powierzchnia_sum} metrów kwadratowych.")
        break

    elif pytanie_wys.lower() == "nie":
        powierzchnia_sum = 0
        wysokosc_1_sciany = float(input("Podaj wysokość pierwszej ściany w metrach: "))
        szerokosc_1_sciany = float(input("Podaj szerokość pierwszej ściany w metrach: "))
        powierzchnia_sum += wysokosc_1_sciany*szerokosc_1_sciany
        ostatnia_sciana = wysokosc_1_sciany

        for i in range (2,ilosc_scian+1):
            wysokosc_input = input(f"Podaj wysokość {i} ściany. Jeśli chcesz przyjąć poprzednią wysokość, wciśniej enter: ")
        
            if wysokosc_input == "":
                wysokosc = ostatnia_sciana
            else:
                wysokosc = float(wysokosc_input)
            szerokosc_input = float(input(f"Podaj szerokość {i} ściany w metrach: "))
            powierzchnia_sum += wysokosc*szerokosc_input
            ostatnia_sciana = wysokosc
        print(f"Powierzchnia ścian do pomalowania wynosi {powierzchnia_sum} metrów kwadratowych.")
        break
            
    else:
        print("To nie była odpowiedź tak lub nie.")

warstwy_gruntu = int(input("Podaj ilość warstw gruntu: "))
warstwy_farby = int(input("Podaj ilość warstw farby: "))

print(f"Potrzebujesz {round(warstwy_gruntu*powierzchnia_sum/5, 2)} litrów gruntu.")
print(f"Potrzebujesz {round(warstwy_farby*powierzchnia_sum/13, 2)} litrów farby.")

# wydajnośc gruntu: 5 mkw = 1 litr
# wydajnośc farby 13 mkw = 1 litr





