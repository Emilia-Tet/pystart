# 1. handler
handler = open('test.txt')
line = handler.readline()

# readline odczytuje jedną linię, readlines więcej linii
print(line)
# ważne żeby zamykać po odczycie
handler.close()

# 2 context manager
with open('test.txt') as handler:
    line = handler.readline()
    print(line)

# 3. zapis do pliku. Na koniec chemy jedną pusta linię.
with open('test.txt', 'w') as handler:
    handler.write('Ala ma kota \n')

# 4. demo
passed = []
with open('oceny.txt', encoding = 'utf-8') as file:
    for line in file:
        first_name, last_name, note = (line.strip()).split(";")
        if note == '2':
            passed.append({'first_name' : first_name, 'last_name' : last_name, 'note' : note})

print(passed)

with open('output.txt', encoding = 'utf-8', mode = 'w') as file:
    for student in passed:
        file.write(f"{student.get('first_name')}; {student.get('last_name')}; {student.get('note')}\n")

# 4b. wersja połączona, ale nie można tak robić jeśli to by miał być jeden plik
with open('oceny.txt', encoding = 'utf-8') as input_file, open('output.txt', encoding = 'utf-8', mode = 'w') as output_file:
    for line in input_file:
        first_name, last_name, note = (line.strip()).split(";")
        if note == '2':
            output_file.write('{first_name}, {last_name}, {note}) \n')
