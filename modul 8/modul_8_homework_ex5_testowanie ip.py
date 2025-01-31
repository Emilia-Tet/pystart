# utwórz bazę danych o nazwie test_ip
# w bazie powinna znaleźć się tabela ip_to_check, 
# która powinna zawierać: jedną kolumnę zawierającą tylko oadresy IP do sprawdzenia
# oraz drugą tabelę log, przechowującą datę sprawdzenia, oraz informację o sukcesie lub porażce

# Adres IP 8.8.8.8 należy do publicznych serwerów DNS Google. 
# Jest to bardzo stabilny i dostępny host, który niemal zawsze odpowiada na żądania sieciowe, 
# dlatego jest często używany do testowania połączenia internetowego lub sprawdzania dostępności hostów.

# int(True) da wartosc 1

import sqlite3
import subprocess
from sys import argv

def get_ips(db_connection):
    cursor = db_connection.cursor()
    res = cursor.execute('SELECT ip FROM ip_to_check')
    return res


def save_status(db_connection, ip: str, is_up: bool):
    cursor = db_connection.cursor()
    cursor.execute('INSERT INTO log(ip, is_up) VALUES(?,?)', (
        ip,
        int(is_up)
    ))

def check_if_is_up(ip: str) -> bool:
    output = subprocess.run(['ping', ip], capture_output=True, shell=True)
    print(output.stdout)
    print(output)
    if 'could not' in output.stdout.decode('utf-8').lower():
        return False
    return True
    # return output.returncode == 0
    # tak podpowiada chat i jeden z uczestników kursu


def initialize(db_connection):
    sqls = ['''CREATE TABLE IF NOT EXISTS ip_to_check(
            ip TEXT
            )''', '''CREATE TABLE log(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TIMESTAP DEFAULT CURRENT_TIMESTAMP,
            is_up INTEGER
            )''']
    cursor = db_connection.cursor()

    for sql in sqls:
        cursor.execute(sql)

    db_connection.commit()


with sqlite3.connect('ip_to_check.db') as connection:
    if len(argv) == 2 and argv[1] == 'setup':
        initialize(connection)

    for ip in get_ips(connection):
        save_status(connection, ip, check_if_is_up(ip))
        print(ip)
        if check_if_is_up(ip):
            print("Działa!")
        else:
            print("Nie działa!")

# check_if_is_up('8.8.8.8')