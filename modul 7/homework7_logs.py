from datetime import datetime
# nie powinnam nazywać tak samo zmiennych i kluczy, bo raz się pomyliłam i nie dałam cudzysłowia

log_list = []
with open('logi_test.txt.txt') as file:
    for row in file:
        if row.strip() == "":
            continue
        date, user, action = row.strip().split(sep=';')
        log_list.append({'date': date, 'user': user, 'action': action})
print(log_list)

savings_dict = {}
for saving in log_list:
    user = saving['user']
    date = saving['date']
    action = saving['action']
    if user not in savings_dict:
        savings_dict[user] = [[date, action]]
    else:
        savings_dict[user].append([date, action])
print(savings_dict)

final_dict = {}
for person in savings_dict:
    full_time = 0
    for i in range(0, len(savings_dict[person])):
        if 'logout' in savings_dict[person][i]:
            during = datetime.strptime((savings_dict[person][i][0]), '%Y-%m-%d %H:%M:%S') - datetime.strptime(savings_dict[person][i-1][0], '%Y-%m-%d %H:%M:%S')
            during_seconds = during.total_seconds()
            full_time += during_seconds
    final_dict.update({person: full_time})

print(final_dict)


# wersja Kacpra jest o wiele prostsza
time_spent = {}
last_seen = {}

with open('logi.txt', encoding='utf-8') as file:
    for line in file:
        row = line.strip().split(';')
        if len(row) != 3:
            continue

        created_at, username, action = row
        created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        print(created_at)

        if action == 'login':
            last_seen[username] = created_at

        if action == 'logout':
            delta = created_at - last_seen[username]
            time_spent[username] = time_spent.get('username', 0) + delta.seconds

for username, spent in time_spent.items():
    print(f"Użytkownik {username} spędził na stronie {spent} s.")


# do wniosków - zapomniałam, że można dodać klucz-value do słownika także po prostu na zasadzie "last_seen[username] = created_at" a nie przez update
# słownik[nowy_klucz] = nowa_wartość jest idealne, gdy dodajesz lub aktualizujesz pojedynczy element.
# słownik.update() jest bardziej odpowiednie, gdy dodajesz lub aktualizujesz wiele elementów na raz lub łączysz dwa słowniki.
# Możesz użyć update() z listą par klucz-wartość lub z innego obiektu iterowalnego.

    
