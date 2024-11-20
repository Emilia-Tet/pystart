from datetime import date, datetime

# Klasa date reprezentuje wyłącznie daty, dlatego nie implementuje metody now(), która wymaga obsługi czasu.
# Klasa datetime obsługuje zarówno daty, jak i czasy, dlatego zawiera metodę datetime.now(), która zwraca aktualną datę i czas.

# 1. date.today()
# Pochodzi z modułu datetime jako metoda klasy date.
# Zwraca bieżącą datę bez informacji o godzinie.
# Format zwracanego obiektu to date, zawiera tylko rok, miesiąc i dzień.

# 2. datetime.now()
# Jest metodą klasy datetime, która jest również częścią modułu datetime.
# Zwraca pełny obiekt datetime, zawierający zarówno datę (rok, miesiąc, dzień), 
# jak i czas (godzinę, minutę, sekundę, mikrosekundy).

today = date.today()
filename = today.strftime(r'%d%m%Y')

products = set()
print("Podaj nazwy produktów, które chcesz dodać do koszyka. Aby zakończyć, wpisz 'koniec'.")
while True:
    product = input("Podaj nazwę produktu: ")
    if product == 'koniec':
        break
    products.add(product)

for product in products:
    with open(f'{filename}.txt', 'a+', encoding='utf-8') as report:
        report.write(product + '\n')


# można też walrusem:
# while (product_name := input("Podaj nazwę produktu: ")) != 'koniec':

# i mozna prościej z wypisaniem ich:
# file.write('\n'.join(products))