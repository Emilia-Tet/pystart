# walrus przypisuje i zwraca wartosc za jednym zamachem
# celem jest skrocenie kodu

# wersja bez morsa

i = 0
while i < 10:
    print(i)
    i = i+1

# wersja z morsem, tutaj nam wyprontuje od 1 a wczesniej od 0 bo dodaje od razu 1

i = 0
while(i:= i+1) < 10:
    print(i)

# to dziala troche jak +=

# wersja bez morsa
n = int(input())
if n % 2 == 0:
    print(f'Liczba {n} jest parzysta.')

# wersja z morsem
if (n:=int(input())) % 2 == 0:
    print(f'Liczba {n} jest parzysta.')

# chodzi o to zeby nie definiowac n w osobnej linii, tylko zrobic to w ramach juz ifa