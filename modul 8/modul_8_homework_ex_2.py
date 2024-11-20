from pathlib import Path
from os import walk

with open('scalone.txt', encoding = 'utf-8', mode = 'a') as output_file:
    for dirpath, dirnames, filenames in walk(r'E:\PROJECTS\pystart\modul 8\modul 8 - homework\modul 8 homework ex 2'):
        print(f"to właśnie widzę: 1.{dirpath}, 2.{dirnames}, 3.{filenames}")
        for filename in filenames:
            file_path = Path(dirpath) / filename
            if file_path.suffix == '.txt':
                with open(file_path, encoding = 'utf-8') as input_file:
                    for line in input_file:
                            output_file.write(line)


# ładne rozwiązanie:

from pathlib import Path
files = [f.name for f in Path('dir_path').iterdir() if f.is_file() and f.suffix == ".txt"]
with open('scalone.txt', 'a') as destination:
    for file in files:
        with open(file, 'r') as source:
            content = source.read()
            destination.write(content)

# i wersja Kacpra, readlines czyta wszystkie naraz a nie po jednej. Znak nowego wiersza na wszelki wypadek na końcu.
from os import walk

with open('scalone.txt', 'w') as output:
    for path, dirs, files in walk('source'):
        for file in files:
            if file.endswith('txt'):
                filename = f'{path}/{file}'
                with open(filename) as source:
                    output.write('\n'.join(source.readlines()))
                    output.write('\n')
