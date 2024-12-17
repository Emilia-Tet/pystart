# przeskanuj pod kątem rozszerzeń (filetype, quantity), potem zrób csv i wykres
import csv
import matplotlib.pyplot as plt
from os import walk
from pathlib import Path

filepath = r'E:\PROJECTS\pystart'
dict_ext = {}

for dirpath, dirnames, filenames in walk(filepath):
    print(f"to właśnie widzę: 1.{dirpath}, 2.{dirnames}, 3.{filenames}")
    for filename in filenames:
        file_path = Path(dirpath) / filename
        ext = file_path.suffix
        ext = ext.replace('.', '')
        print(ext)
        dict_ext[ext] = dict_ext.get(ext, 0)+1

print(dict_ext)

figure, axes = plt.subplots()
# 2 wiersze (1 kolumna), więc wykresy będą jeden nad drugim
extensions = dict_ext.keys()
amounts = dict_ext.values()
axes.set_xlabel('Extensions')
axes.set(ylabel='Amounts', title='Extensions in Pystart course')
axes.bar(extensions, amounts)


# można też uyć DictWritera w tej sytuacji
for key, value in dict_ext.items():
    with open('report.csv', 'a', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow([f'{key}, {value}'])


plt.show()
    