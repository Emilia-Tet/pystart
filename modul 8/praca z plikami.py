# nie warto parsowac dir ani ls
# walk zwraca tuple z 3 elementami
# przechodzi rekursywnie po wszystkim 


# dirpath – ścieżka do bieżącego katalogu, który jest przetwarzany.
# dirnames – lista nazw podkatalogów znajdujących się w bieżącym katalogu (dirpath).
# filenames – lista nazw plików znajdujących się w bieżącym katalogu (dirpath).
# Szczegóły:
# dirpath: Jest to pełna ścieżka do katalogu, w którym obecnie znajduje się os.walk(). 
# Za każdym razem, gdy funkcja przechodzi do innego katalogu, dirpath jest aktualizowane na ścieżkę do tego katalogu.

# dirnames: Zawiera listę nazw podkatalogów w bieżącym katalogu (dirpath). 
# Możesz modyfikować tę listę, jeśli chcesz zmienić sposób, 
# w jaki os.walk() przetwarza kolejne podkatalogi (np. wykluczyć pewne katalogi z przeszukiwania).

# filenames: Zawiera listę nazw plików w bieżącym katalogu (dirpath). 
# Lista ta nie zawiera pełnych ścieżek do plików, ale same nazwy plików. 
# Aby uzyskać pełną ścieżkę, należy połączyć dirpath z filename za pomocą os.path.join() lub Path z modułu pathlib.

from os import walk

for dir, directories_in_dir, files_in_dir in walk(r'E:\PROJECTS\TADZIO'):
    print(dir, directories_in_dir, files_in_dir)


# sprawdzanie rozszerzeń
# 1. mało prof, ale raczej działa - filename.endswith('.pdf')
# 2. z komentarza, w ramach os: os.path.splitext(file)
# 3. biblioteka pathlib

from pathlib import Path
# uwaga, jeśli plik istnieje w innym folderze niż skrypt, to musze podać pełną sciężkę
# file = Path(r'Lekcja 1. Crafting Table (Szablon)2.sb3')
file = Path(r'E:\PROJECTS\TADZIO\giganci programowania\Lekcja 1. Crafting Table (Szablon)2.sb3')

# rozszerzenie pliku
print(file.suffix)

# czy plik istnieje
print(file.exists())

# ścieżka bezwzględna do pliku
print(file.resolve())

# true lub false czy jest to folder czy plik
print(file.is_file())
print(file.is_dir())