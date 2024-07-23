# chce zaktualizować json o nowego autora
# najpierw muszę załadować te dane
# read działa inaczej niż load, bo load ładuje listę, a read wyświetla znaki końca linii
# uwaga na klucze żeby były takie same, inaczej będzie bałagan
# jeśli json będzie pusty, to pojawi się dziwny błąd że expecting value 

from json import load, dump

new_author = "Witold Gombrowicz"
new_title = "Ferdydurke"

with open("books.json") as file:
    # print(file.read())
    books = load(file)

for book in books:
    print('Tytuł', book.get('title'))
    print('Autor', book.get('author'))
    print('--'*10)

with open('books.json', 'w') as file:
    books.append({
        'title': new_title,
        'author': new_author
    })
    dump(books, file)



new_author = input("Podaj autora")
new_title = input("Podaj tytuł")

with open('books.json', 'w') as file:
    books.append({
        'title': new_title,
        'author': new_author
    })
    dump(books, file)

# inputa lepiej nie dawać w samym with open, bo jeśli ktoś nic nie poda to wyczyści mi cały plik w trybie write. 
# a nie mozna dawać trybu "a", z uwagi na spójność pliku json.
