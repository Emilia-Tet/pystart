# pobieraj dane pogodowe raz dziennie do bazy danych

# Kacper zrobił created_at jako TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# więc się samo uzupełnia

from requests import get
import sqlite3
from datetime import date

today = date.today()
date_name = today.strftime(r'%d%m%Y')
today_done = False

with sqlite3.connect('meteo.db') as connection:
    sql = ''' CREATE TABLE IF NOT EXISTS meteo(
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    city TEXT NOT NULL,
    temperature FLOAT,
    pressure FLOAT
    )'''

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

# sprawdź, czy już istnieje taki rekord w bazie danych
with sqlite3.connect('meteo.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM meteo WHERE date = ?", (date_name,))
    row = cursor.fetchone()
    if row:
        today_done = True
        print("Jest już taki rekord")
        print(row)
    else:
        pass

if not today_done:
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    data = response.json()
    codes = ['temperatura', 'cisnienie']
    for synop_dict in data:
        if synop_dict['stacja'] == 'Warszawa':
            print(synop_dict['temperatura'], synop_dict['cisnienie'])
            cursor.execute(
                'INSERT INTO meteo(date, city, temperature, pressure) VALUES(?, ?, ?, ?)', 
                (date_name, 'Warszawa', synop_dict['temperatura'], synop_dict['cisnienie'])
                )
            connection.commit()

