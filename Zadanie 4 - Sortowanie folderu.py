# os - operating system

import os

for cos in os.walk('.'):
    print(cos)

for glowny_katalog, katalog, pliki in os.walk('.'):
    for plik in pliki:
        print(plik)