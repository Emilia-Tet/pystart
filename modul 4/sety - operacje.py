# suma | ("pipe")
# roznica -
# iloczyn & ("amperasnd") --> czesc wspolna
# roznica symetryczna ^ ("karetka") --> wszystko poza czescia wspolna

# odejmujac uwazajmy co od czego odejmiemy, bo wynik sie bedzie roznil ;-) 

# zadanie 1
podzielne_3 = set([i for i in range(101) if i%3 ==0])
podzielne_5 = set([i for i in range(101) if i%5 ==0])

#KAcepr zrobil i to jest lepsze:
podzielne_3 = set(range(3,101,3))
podzielne_5 = set(range(5,101,5))

podzielne_3_i_5 = podzielne_3 & podzielne_5
print(podzielne_3_i_5)


# zadanie 2
word1 = set("kaczka")
word2 = set("kukuryku")
not_common_signs = word1^word2
print(not_common_signs)

# zadaie 3
students = {
    ("Katarzyna", "Gorska"),
    ("Piotr", "Kowalski"),
    ("Tomasz", "Adamski"),
    ("Joanna", "Mazur"),
    ("Aleksander", "Alkowski")
}

going_on_trip = {
    ("Tomasz", "Adamski"),
    ("Joanna", "Mazur"),

}

staying_at_school = students - going_on_trip
str_names = ""
print("W szkole zostaja:")
for index, (name, surname) in enumerate(staying_at_school):
    print(name, surname, end = "")
    if index < len(staying_at_school) -1:
        print(",", end = " ")