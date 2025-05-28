# tu wcale nie dodajemy „nowego typu danych” do argparse’a, 
# tylko używamy wbudowanej opcji type= przy add_argument(), 
# która przyjmuje funkcję konwertującą/parsującą wartość przekazaną z linii poleceń.
# ex:
# def square(x):
#     return int(x)**2

# parser.add_argument('--number', type=square)


import sys
import argparse
from datetime import datetime

def valid_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise argparse.ArgumentTypeError("Data musi być w formacie rrrr-mm-dd")

class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Zarządzanie budżetem domowym')

        self.action_group = self.parser.add_mutually_exclusive_group(required=True)
        self.action_group.add_argument(
            '--add-expense',
            dest='action',
            action = 'store_const',
            const = 'add_expense',
            help = 'Dodawanie wydatku'
        )
        self.action_group.add_argument(
            '--add-income',
            dest='action',
            action = 'store_const',
            const = 'add_income',
            help = 'Dodawanie przychodu'
        )

        self.action_group.add_argument(
            '--delete',
            dest='action',
            action = 'store_const',
            const = 'delete',
            help = 'Usuwanie wydatku lub przychodu'
        )

        self.action_group.add_argument(
            '--stats',
            dest='action',
            action = 'store_const',
            const = 'stats',
            help = 'Wyświetlanie statystyk'
        )

        self.action_group.add_argument(
            '--list',
            dest='action',
            action = 'store_const',
            const = 'list',
            help = 'Wyświetlanie wpisów'
        )

        self.add_group = self.parser.add_argument_group('Dodawanie elementu pryzchodu lub wydatku')
        self.add_group.add_argument(
            '--name',
            type=str,
            help='Nazwa elementu',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.add_group.add_argument(
            '--category',
            type=str,
            help='Nazwa kategorii',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )
        self.add_group.add_argument(
            '--date',
            type=valid_date,
            help='Data wystąpienia wydatku lub przychodu w formacie rrrr-mm-dd',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )

        self.add_group.add_argument(
            '--value',
            type=float,
            help='Wartość',
            required='--add-expense' in sys.argv or '--add-income' in sys.argv
        )

        self.delete_group = self.parser.add_argument_group('Usuwanie elementu')
        self.delete_group.add_argument(
            '--id', 
            type=int, 
            help='Identyfikator elementu',
            required='--delete' in sys.argv)

    def parse_args(self):
        return self.parser.parse_args()