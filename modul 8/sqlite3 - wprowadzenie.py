# CREATE TABLE IF NOT EXISTS: To zapytanie SQL utworzy tabelę books tylko wtedy, 
# gdy jeszcze nie istnieje, dzięki czemu unikniemy błędu w przypadku, gdy tabela już została utworzona.
# AUTOINCREMENT przy id INTEGER PRIMARY KEY AUTOINCREMENT zapewnia, 
# że id automatycznie zwiększa się o 1 przy każdej nowej książce.
# commit(): Zatwierdzamy zmiany, aby zapisano dane w bazie.


import sqlite3

# można tak:
connection = sqlite3.connect('library.db')
connection.close()

# można przez context managera
with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    ''')

    title = input('Tytuł: ')
    author = input('Autor: ')
    cursor.execute('INSERT INTO books VALUES (null, ?, ?)', (title, author))
    connection.commit()


with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    
    # Wybieramy wszystkie rekordy z tabeli `books`
    cursor.execute('SELECT * FROM books')
    
    # Pobieramy wyniki zapytania
    rows = cursor.fetchall()
    
    # Sprawdzamy, czy w tabeli są jakieś rekordy
    if rows:
        print("Zawartość tabeli 'books':")
        for row in rows:
            print(row)
    else:
        print("Tabela 'books' jest pusta.")
