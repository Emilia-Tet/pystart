from json import load, dump
# bardziej złożona wersja, to utworzenie klasy dziedziczącej po parserze dla 'Person'. 
# Ale tutaj jest ta prostsza wersja.
# KLIKNIĘCIE DWA RAZY I APOSTROF DODAJE APOSTROFY WOKÓŁ!!!!!

#biblioteka Pydantic by za mnie opisała słownik w add_element

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class JsonParser:
    def __init__(self, filename: str):
        try:
            with open(filename) as file:
                content = load(file)
        except FileNotFoundError:
            content = []

        self.content = content
        self.filename = filename

    def get_data(self):
        return self.content
    
    def add_element(self, element: Person):
        self.content.append({
            'first_name': element.first_name,
            'last_name': element.last_name
        })

        with open(self.filename, 'w') as file:
            dump(self.content, file)

    
person = Person('James', 'Callaghan')

file = JsonParser('data.json')
file.get_data()
file.add_element(person)