# np init wyświetla się, kiedy tworzony jest obiekt
# __str__ reprezentacja tekstowa
# __add__ dodanie obiektów, np list
# __eq__ porównanie ==
# __ge__ porównanie >= (greater equal)
# __le__ porównanie <= (less equal)
# __ne__ nierówne
# są takie obiekty, które mogą być callable jak funkcje

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

me = Person('Test', 'Testowski')
print(me)


class Box:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def __add__(self, other):
        total = self.capacity + other.capacity
        return Box(total)
    
    def __eq__(self, other):
        return self.capacity == other.capacity
    

# dodać opcję dodawania, odejmowania i porównywania obiektów:
class Lenght_Unit:
    def __init__(self, value: int):
        self.value = value

    def to_centimeter(self):
        return self.value / 10
    
    def to_meter(self):
        return self.value / 10 / 100
    
    def __add__(self, other):
        total = self.value + other.value
        return Lenght_Unit(total)
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __sub__(self, other):
        total = self.value - other.value
        return Lenght_Unit(total)
    
    def __str__(self):
        return f'{self.value} mm'
    
    def __gt__(self, other):
        return self.value > other.value
    
v1 = Lenght_Unit(300)
v2 = Lenght_Unit(750)
v5 = Lenght_Unit(300)

print(v1)
print(v2)
print(v1-v2)    

print(v1==v5)
print(v1!=v5)