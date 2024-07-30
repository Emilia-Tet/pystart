# 'x' - tryb tworzenia (exclusive creation). Plik zostanie utworzony, jeśłi dotąd nie istnieje. 
# jeśli istnieje, Python zgłosi FileExistsError.


import csv
# iterujemy nie po samym csvfile, a po obiekcie reader
# quotechar: jeżeli w ramach tych znaków (tutaj "") pojawi się delimiter,
# to nie będzie traktowany jako delimiter tylko zwykły znak

with open('orders.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(row)

with open('orders.csv', 'a', newline='') as csvfile:
    writer = csv.reader(csvfile, delimiter=';', quotechar='"')
    writer.writerow([4, 'Test', 'Testowski'])

# żeby row był słownikiem a nie listą
# kolumny muszą mieć unikatowe nazwy

with open('orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        print(row['first_name'], row['last_name'])

# analogicznie można zapisywać:
with open('orders.csv', mode='w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'first_name': 'Test', 'last_name': 'Testowski'})
