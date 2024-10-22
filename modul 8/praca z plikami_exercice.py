# Cudzysłowy są potrzebne, gdy ścieżka do katalogu zawiera spacje lub inne specjalne znaki, 
# aby uniknąć problemów z interpretacją wiersza poleceń. 
# W przypadku rozszerzenia pliku (np. jpg) cudzysłowy nie są wymagane, 
# ponieważ nie zawiera ono spacji ani znaków specjalnych, więc wiersz poleceń może poprawnie je odczytać.

# Dwa myślniki (--): Używa się ich do argumentów nazwanych, 
# które zazwyczaj mają dłuższe i bardziej opisowe nazwy, np. --directory, --extension.
# Jeden myślnik (-): Jest stosowany dla skróconych wersji argumentów, takich jak -d dla --directory lub -e dla --extension. 
# Krótsze wersje argumentów są przydatne, gdy chcemy szybciej wpisać komendę.


# w argparse można zdefiniować argumenty pozycyjne, które nie wymagają żadnych myślników. 
# Argumenty pozycyjne są wymagane i muszą być podane w określonej kolejności podczas wywoływania programu. 
# W przeciwieństwie do argumentów nazwanych, ich wartości są przypisywane na podstawie pozycji, w której się znajdują w linii poleceń.
# python nazwa_programu.py C:\Users\Documents txt


import argparse
from os import walk
from pathlib import Path
import logging
# najpierw tworzymy dokumentację wyjaśniającą czym jest nasz program, opisujemy które argumenty są wymagane, które opcjonalne

parser = argparse.ArgumentParser(
    prog='Files report',
    description='This app shows you all files with a given extension',
    epilog='Author: Test Testowski'
)

parser.add_argument('--directory', required=True, help='Path to the directory')
parser.add_argument('--extension', default='jpg', help='File extension to search for')

args = parser.parse_args() # bardzo ważna linia, zbiera od użytkownika to co on wpisze
print(args)

for dirpath, dirnames, filenames in walk(args.directory):
    print(f"to właśnie widzę: 1.{dirpath}, 2.{dirnames}, 3.{filenames}")
    for filename in filenames:
        file_path = Path(dirpath) / filename
        if file_path.suffix == f'.{args.extension}':
            print(file_path)
            print(file_path.absolute())


logging.info(f"dirpath: {dirpath}")

# to właśnie widzę: 1.E:\PROJECTS\TADZIO\giganci programowania, 2.[], 3.['Lekcja 1. Crafting Table (Szablon).sb3', 'Lekcja 1. Crafting Table (Szablon)2.sb3']

# / operator jest specjalnym operatorem przeciążonym w klasie Path z modułu pathlib, 
# który łączy ścieżki. W efekcie, gdy wykonujesz Path(dirpath) / filename, 
# operator / łączy katalog (dirpath) z nazwą pliku (filename), tworząc pełną ścieżkę. 
# Nawet jeśli dirpath lub filename zawiera spacje, konstrukcja Path to obsłuży poprawnie.