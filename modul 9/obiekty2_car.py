# ten przykład pokazuje w jaki sposób można pomieszać słownik z obiektem

class Car:
    def __ini__(self, name: str, price: float, speed: float):
        self.name == name
        self.price == price
        self.speed = speed


cars = []

for i in range(0, 5):
    ask_name = input("Podaj nazwę samochodu: ")
    ask_price = input("Podaj cenę samochodu: ")
    ask_speed = input("Podaj maksymalną prędkość samochodu: ")
    cars.append({'name': ask_name, 'price': ask_price, 'speed': ask_speed})

print(cars)

cars2 = []

for _ in range(6):
    cars2.append(Car(input("Podaj nazwę samochodu: "), input("Podaj cenę samochodu: "), input("Podaj maksymalną prędkość samochodu: ")))

for car in cars2:
    print(f'{car.name}, cena: {car.price}, prędkość maksymalna: {car.speed}.')

# Słowniki: Lepsze dla prostych, dynamicznych i jednorazowych struktur danych.
# Obiekty: Lepsze dla złożonych, dobrze zorganizowanych struktur z logiką biznesową i wielokrotnym użyciem.
# Wybór między słownikiem a obiektem zależy więc od Twoich specyficznych potrzeb dotyczących struktury danych, ich użycia oraz złożoności projektu.
# dodatkowo obiekty mają opcję: Encapsulacja: Gdy chcesz ukryć wewnętrzne szczegóły implementacji i kontrolować dostęp do danych.
