# argparse to moduł wbudowany w język Python, który służy do tworzenia interfejsów wiersza poleceń. 
# Umożliwia dodawanie opcji i argumentów do skryptów Pythona, 
# dzięki czemu można je wywoływać z różnymi parametrami bez konieczności zmiany kodu źródłowego. 
# Dzięki argparse skrypt automatycznie generuje pomoc (--help lub -h), pokazując dostępne argumenty oraz ich opisy:
# python script.py --help



import argparse

# najpierw tworzymy dokumentację wyjaśniającą czym jest nasz program, opisujemy które argumenty są wymagane, które opcjonalne

parser = argparse.ArgumentParser(
    prog='Image Resizer',
    description='This is a sample application',
    epilog='Author: Test Testowski'
)


parser.add_argument('path', type=str)
parser.add_argument('target', type=str)
parser.add_argument('--width', default=300, type=int)
parser.add_argument('--height', default=300, type=int)

arguments = parser.parse_args()
print('path', arguments.path)
print('target', arguments.target)
print('width', arguments.width)
print('height', arguments.height)