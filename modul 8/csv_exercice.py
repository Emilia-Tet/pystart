import csv

cars_dict = [
    {'name': 'Hennessey Venom F5', 'time_to_100': 2.6, 'speed_record': 484},
    {'name': 'SSC Tuatara', 'time_to_100': 2.5, 'speed_record': 460},
    {'name': 'Koeningsegg Agera RS', 'time_to_100': 3.1, 'speed_record': 457},
    {'name': 'Koeningsegg One 1', 'time_to_100': 2.6, 'speed_record': 450},
]

# newline sprawia, że nie ma pomiędzy wierszami pustej linii
with open('fast_cars.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'time_to_100', 'speed_record']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # żeby zobaczyć nagłówek:
    writer.writeheader()
    for row in cars_dict:
        # tak prościej niż -> writer.writerow(row['name'], row['time_to_100'], roq['speed_record'])
        # ale daje ten sam efekt
        writer.writerow(row)

with open('fast_cars.csv') as readfile:
    reader = csv.DictReader(readfile, delimiter=',')
    for row in reader:
        # print(row['name'], row['time_to_100'], roq['speed_record'])
        print(row)
        
