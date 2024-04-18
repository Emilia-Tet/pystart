from random import choice

 

info = {"Francja" : "Paryz",

        "Niemcy" : "Berlin",

        "Szwajcaria" : "Bern",

        "Polska" : "Warszawa",

        "Ukraina" : "Kijow",

        "USA" : "Nowy Jork",

        "Belgia" : "Bruksela"}

 

 

result = 0

used_countries = []

for i in range(0,3):

    while True:

        random_choice = choice(list(info.items()))

        type(random_choice)

        if random_choice[0] not in result:

            break

   

    users_choice = input(f"Podaje stolice kraju: {random_choice[0]}. ")

    used_countries.append(random_choice[0])

    if users_choice == info[random_choice[0]]:

        print("Dobrze!")

        result += 1

    else:

        print("Zle :(")

  

 

if result == 0:

    print("0 punktow, nastepnym razem pojdzie ci lepiej")

elif result == 1:

    print("Jeden punkt na otarcie lez")

elif result ==2:

    print("2 punkty, tylko jeden blad!")

else:

    print("Bezblednie ci poszlo!")