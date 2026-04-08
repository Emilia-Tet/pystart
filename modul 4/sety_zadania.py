# zadanie 1

numbers = []

while len(numbers) <10:
    try:
        number = int(input("Podaj liczbe calkowita wieksza od 0: "))
        if number >= 0:
            numbers.append(number)
        else:
            print("To byla liczba ujemna, nie zostanie dodana do listy.")
    except:
        print("To nie byla liczba calkowita, sprobuj jeszcze raz")
print(numbers)
print(f"Najmniejsza z podanych liczb to {sorted(numbers)[0]}, "
      f"a najwieksza to {sorted(numbers)[-1]}.")

# mozna tez uzyc min(numbers i max(numbers))

# zadanie 2
# mozna zrobic zmienna o wartosci None

liczby = []
try: 
    pierwsza_liczba = int(input("Podaj dowolna liczbe calkowita: "))
    liczby.append(pierwsza_liczba)
except:
    print("To nie byla liczba calkowita...")


while True:
    liczba = int(input("Podaj liczbe calkowita, ktora bedzie wieksza od poprzedniej: "))
    if liczba > liczby[-1]:
        liczby.append(liczba)
    else:
        print(f"Ta liczba nie byla wieksza od poprzedniej, nie zostanie dodana do listy. " 
              f"Koncze zliczanie. Srednia z podanych liczb to: {sum(liczby)/len(liczby):.2f}.")
        break
        

# zadanie 3
from random import randint
print("Ta gra polega na odgadnieciu losowo wybranej liczby od 1 do 1000. "
      "Sprobuj zgadnac, a ja bede dawac wskazowki.")

random_int = randint(1, 1000)
counter = 0

while True:
    users_int = int(input("Sprobuj zgadnac: "))

    if users_int < random_int:
        print("Podales za mala liczbe.")
        counter +=1

    elif users_int > random_int:
        print("Podales za duza liczbe.")
        counter +=1

    else:
        print(f"Tak jest! Brawo! Zgadles po {counter} probach!")
        break
