# UWAGA! w skryptach webowcyh uwaga na to co użytkownik wprowadza i co będzie wywołane w poleceniu systemowym
# użytkownik może np włamać się na serwer z poziomu przeglądarki

# automatyzacja, np wykonywanie poleceń w określonym czasie
# intgrowanie narzędzi, które nie udostępniają API
# uruchamianie i zatrzymywanie programów
# kontrolowanie procesów uruchomionych przez pythona
# wykonywanie poleceń, np. ping

# np. wykonywanie backupu danych
# automatyczne pobieranie plików z konkretnego adresu
# sprawdzanie listy aktualnie włączonych procesów (tasklist)

import subprocess

# tak dostaniemy tylko info w terminalu
subprocess.run('ls', shell=True)

# a tak zmienna przechowa info
# możemy chcieć zatrzymać proces o konkretnej nazwie
result = subprocess.run(["ls", '-l'], shell=True, capture_output=True)
print(result.stdout.decode('utf8'))

# '-l', 'ls'

# zadanie 1

# PS E:\PROJECTS\pystart\modul 8> ping pystart.pl

# Pinging pystart.pl [109.95.159.3] with 32 bytes of data:
# Reply from 109.95.159.3: bytes=32 time=18ms TTL=58
# Reply from 109.95.159.3: bytes=32 time=15ms TTL=58
# Reply from 109.95.159.3: bytes=32 time=22ms TTL=58
# Reply from 109.95.159.3: bytes=32 time=38ms TTL=58

# Ping statistics for 109.95.159.3:
#     Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
# Approximate round trip times in milli-seconds:
#     Minimum = 15ms, Maximum = 38ms, Average = 23ms


# Ping zazwyczaj wyświetla statystyki, takie jak czas potrzebny na przesłanie pakietów tam i z powrotem (w milisekundach), procent utraconych pakietów oraz liczba wysłanych i odebranych pakietów. Można również zobaczyć wartość TTL (Time to Live) pakietów, która wskazuje, ile routerów (skoków) pakiet przebył.

domain = input("Podaj adres do sprawdzenia: ")
output = subprocess.run(['ping', '-n', '1', domain], shell=True, capture_output=True)
print(output)