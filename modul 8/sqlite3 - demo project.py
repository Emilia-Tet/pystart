import sqlite3
from sys import argv

#dbeaver - universal database tool

# cursor to obiekt, który służy do wykonywania zapytania
# na kursorze wykonuje się (execute) queries
# natomiast na samym pliku jeszcze wykonuje się commit, żeb coś do nich dodać

# to daje setup
# PS E:\PROJECTS\pystart\modul 8> python '.\sqlite3 - demo project.py' setup
# Traceback (most recent call last):
#   File "E:\PROJECTS\pystart\modul 8\sqlite3 - demo project.py", line 23, in <module>
#     setup()
#   File "E:\PROJECTS\pystart\modul 8\sqlite3 - demo project.py", line 19, in setup
#     cursor.execute(sql)
# sqlite3.OperationalError: table BOOKS already exists

def setup():
    with sqlite3.connect('books.db') as connection:
        sql = ''' CREATE TABLE BOOKS(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100) UNIQUE NOT NULL,
        author VARCHAR(100)
        )'''

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

if len(argv) == 2 and argv[1] == 'setup':
    setup()

with sqlite3.connect('books.db') as connection:
    cursor = connection.cursor()
    for book in cursor.execute('SELECT book_id, title, author FROM books'):
        print(book)
    
    title = input('Podaj tytuł: ')
    author = input('Podaj imię i nazwisko autora: ')

    cursor.execute(
        'INSERT INTO books(title, author) VALUES(?, ?)', 
        (title, author)
    )
    connection.commit()