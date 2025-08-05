from datetime import datetime

with open("dane.txt") as plik:
    dane = plik.readlines()

wynik = []
for wiersz in dane:
    imie, nazwisko, data_urodzenia = wiersz.strip().split(',')
    data_urodzenia = datetime.strptime(data_urodzenia, '%d.%m.%Y').strftime('%Y-%m-%d')

    wynik.append((
        data_urodzenia, 
        imie, 
        nazwisko, 
        ))
    
wynik.sort(key=lambda x: x[0])

with open("wyniki.txt", "w") as plik_wynik:
    for linia in wynik:
        plik_wynik.write(','.join(linia) + '\n')
