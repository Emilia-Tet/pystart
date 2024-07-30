# nie zawsze chcemy podawać argumenty w samej treści programu - wtedy argparse
# pozwala uruchomić program od razu z argumentami
# żeby uruchomić:
# python my_program.py --name=Kacper --age 18
# obojętnie czy znak równości czy spacja
# to nam tworzy tzw programy klienckie czyli CLI
# python my_program.py -h, ta komenda wyświetli pomoc czyli arkusz z listą, wyjaśniającą nam czym jest name, age i inne argumenty

import argparse

# najpierw tworzymy dokumentację wyjaśniającą czym jest nasz program, opisujemy które argumenty są wymagane, które opcjonalne

parser = argparse.ArgumentParser(
    prog='Hello World!',
    description='This is a sample application',
    epilog='Author: Test Testowski'
)

parser.add_argument('name') # ten argument jest wymagany
parser.add_argument('-l', '--lastname') # ten argument jest opcjonalny
# definiuje argument, który może być przekazany do skryptu w dwóch formach
# jako krótka opcja z pojedynczym myślnikiem -l oraz jako długa z podwójnym myślnikiem --lastname.
# przykłąd użycia w linii poleceń: python skrypt.py -l Kowalski
parser.add_argument('-a', '--admin', action='store_true') # też opcjonalny, z założenia jest tym adminem
parser.add_argument('-y', '--year', type=int) # można z góry określić też data type

args = parser.parse_args() # bardzo ważna linia, zbiera od użytkownika to co on wpisze
print(args)
print(args.name)
