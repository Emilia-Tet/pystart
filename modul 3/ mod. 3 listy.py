fruits = ["mango", "banana", "apple", "grapefruit", "lemon"]
fruits.remove("mango")
print(fruits)

# WAŻNE The del keyword is used to delete objects. In Python everything is an object, so the del keyword can also be used to delete variables, lists, or parts of a list etc.
del fruits[3]
print(fruits)

bands = ["The Beatles", "Femme", "Bonobo"]
bands[0] = "The White Stripes"
print(bands)
del bands[0]
print(bands)
bands.append("The Beatles")
bands.append("The White Stripes")
print(bands)

"Femme" in bands
# jeżeli zamienię literę na małą, to już mi powie False
"femme" in bands

"Deep Purple" in bands
bands.remove("The Beatles")
print(bands)

# zrobienie listy ze stringu dzieli na osobne litery
napis = "I like music"
napis = list(napis)

# mogę wtedy podmienić jakąś literę w liście
del napis[5]
napis[4] = "q"
print(napis)

# nie da się tego złączyć ponownie za pomocą str(napis), bo wrzuci mi w str całą listę włącznie ze wzystkimi apostrofami itd. 
# ale można tak:
napis = ''.join(napis)

first_names = ["Asia", "Basia", "Wojtek", "Krysia"]
first_names.append("Krzysztof")
first_names.insert(3, "Krzysztof")
first_names.remove("Krzysztof")
last_first_name = first_names.pop()
third_name = first_names.pop(2)
# całkiem czyści listę
first_names.clear()

# mapowanie elementów listy - modyfikacja każdego z nich
names = ["aSiA", 'basIa', "wOJteK", "KRYsiA"]
proper_names = []
for name in names:
    proper_names.append(name.title())

# albo moja próba - działa, tylko trzeba pamiętać żeby zamienić z powrotem na listę
names = ["aSiA", 'basIa', "wOJteK", "KRYsiA"]
proper_names = list(map(lambda name: name.title(), names))
print(proper_names)

# filtrowanie
male_names = []
for name in proper_names:
    if not name.endswith('a'):
        male_names.append(name.title())

# albo inaczej
male_names = list(filter(lambda name: name.endswith('a') != True, proper_names))
print(male_names)

# sorted zwraca nową listę, posortowaną
# metoda .sort modyfkuje istniejącą listę

for name in sorted(proper_names):
    print(name)

proper_names.sort(reverse = True)
for name in proper_names:
    print(name)

# listy można mnożyć i dodawać, ale nie odejmować. Dostajemy wtedy nową, inną listę. Jeśli chcemy zachować tę samą, to używamy entend
cities = ["Sopot", "Warszawa"] + ["Kraków"]
small_cities = ["Konin", "Leszno"]
cities.extend(small_cities)

# zip pozwala przejś po kilku listach naraz
countries = ["Poland", "France", "Germany"]
capitals = ["Warsaw", "Paris", "Berlin"]
for country, capital in zip(countries, capitals):
    print(country, '-', capital)
