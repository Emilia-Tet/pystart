# są dwie opcje, utworzyć zmienną i w niej przechować edytowany tekst i potem podmienić
# albo utworzyć drugi plik i zmienić mu nazwę
# tu plik jest nieduży, więc mozna to pierwsze

tempo_list = []
with open('balagan.txt', 'r', encoding='utf-8') as file:
    for line in file:
        tempo_list.append(line)


for i, phrs in enumerate(tempo_list):
    if 'Java' in phrs and 'Java Script' not in phrs:
        tempo_list[i] = phrs.replace('Java', 'Python')
print(tempo_list)


# Kacper prościej:

correct_lines = []

with open('balagan.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if 'Java Script' not in line:
            line = line.replace('Java', 'Python')

        correct_lines.append(line.strip())
print(correct_lines)

with open('balagan.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(correct_lines) + '\n')
