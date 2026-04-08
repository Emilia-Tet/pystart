# wstep

person = ("Jan", "Kowalski")
match person:
    case("John", "Kowalski"):
        print("Czesc Johnie Kowalski!")
    
    case("Jan", last_name):
        print(f"Czesc Janie o nazwisku {last_name}")


    case(first_name, "Kowalski"):
        print(f"Czesc kolego Kowalski o imieniu {first_name}.")

    case _:
        print("Jeszcze sie nie znamy, powiedz cos o sobie.")





# wersja 1 : dictionnary

months = ["January", "February", "March", "April", "May", "June", "July", "August"]
months_dict = {i+1: month for i, month in enumerate(months)}
# faktycznie dict powinien miec dwie czesci rozdzielone : i tak tutaj jest
users_choice = int(input("Podaj cyfre od 1 do 12 zeby dowiedziec sie, jaki to miesiac w roku: "))
try:
    print(f"Podana liczba odpowiada miesiacowi: {months_dict[users_choice]}")
except:
    print("Podales liczbe, ktora nie odpowada zadnemu miesiacowi w roku.")

# wersja 2 : match case

users_choice = int(input("Podaj cyfre od 1 do 12 zeby dowiedziec sie, jaki to miesiac w roku: "))
month_text_text = None
match users_choice:

    case 1: month_text = 'January'
    case 2: month_text = 'February'
    case 3: month_text = 'March'
    case 4: month_text = 'Avril'
    case 5: month_text = 'May'
    case 6: month_text = 'June'
    case 7: month_text = 'July'
    case 8: month_text = 'August'
    case 9: month_text = 'September'
    
    case _:
        print("Podales liczbe, ktora nie odpowada zadnemu miesiacowi w roku.")
        quit()
print(f"Podany miesiac to {month_text}.")

