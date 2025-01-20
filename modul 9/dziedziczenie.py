# dziedzicze dajac w nawiasie parenta
class Parent():
    def __init__ (self):
        pass

class Child(Parent):
    def __init__ (self):
        pass

# metody beda kopiowane
class Parent():
    def __init__ (self):
        pass

    def get_type(self):
        return 'Hooman'

class Child(Parent):
    def __init__ (self):
        pass

child = Child()
print(child.get_type())

# chyba, ze je nadpiszemy
class Parent():
    def __init__ (self):
        pass

    def get_type(self):
        return 'Hooman'
    
    def get_details(self):
        return 'tall'

class Child(Parent):
    def __init__ (self):
        pass

    def get_details(self):
        return 'small'
    
new_child = Child()
print(new_child.get_details())


# mozna tez skorzystac z tego, co wyliczyl rodzic, ale to skonfigurowac dodatkowo 
# za pomoca super()
# super(): biore metode z klasy, po ktorej dziedzicze
# self: biore metode z klasy, w ktorej aktualnie jestem, chocby byla odziedziczona z rodzica

class Parent():
    def __init__ (self):
        pass

    def get_type(self):
        return 'Hooman'
    
    def get_details(self):
        return 'tall'

class Child(Parent):
    def __init__ (self):
        pass

    def get_type(self):
        basic_type = super().get_type()
        return 'small' + ' '+ basic_type

    def get_details(self):
        return 'small'
    
new_child = Child()
print(new_child.get_type())

# __init__ zachowa sie tak jak kazda inna metoda - tez sie odziedziczy

class Rodzic:
    def __init__(self):
        print('Rodzic!')

class Dziecko(Rodzic):
    pass

dziecko = Dziecko()

# jezeli przykrywamy init rodzica w inicie dziecka, to powinnismy skorzystac z super, no chyba ze 
# swiadomie naprawde nie chcemy zeby sie przekopiowal

class Person:
    def __init__(self, first_name, last_name):
        self.details = f'{first_name} {last_name}'

class Student(Person):
    def __init__(self, first_name, last_name, semester):
        super().__init__(first_name, last_name)
        self.semester = semester


jan = Student('Jan', 'Kowalski', 2)
print(jan.details)
print(jan.semester)