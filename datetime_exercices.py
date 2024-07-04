from datetime import date, timedelta, datetime



# iso format najlepszy do baz danych
# wiecej formatów na stronie https://docs.python.org/3/library/datetime.html#strftime-and-strptime
# p jak paroswanie (strptime)

today = date.today()
print(f"Today is {today}")

formatted_today = today.strftime("%d.%m.%Y")
# strf = string formatted
print(f"Today is {formatted_today}")

bd_day = date(today.year, 11, 9)
bd_formatted = bd_day.strftime("%d.%m.%Y, %A")
print(f"Moje urodziny w tym roku wypadają {bd_formatted}.")

today = date.today()
bd_day = date(today.year, 11, 9)

if bd_day > today:
    diff = bd_day - today
    print(f"Do urodzin pozostało {diff.days} dni.")
#diff samo w sobie jest obiektem 

else:
    diff = today - bd_day
    print(f"Urodziny były {diff.days} dni temu.")

# zadanie 1



def bd_alert(given_mth, given_day):
    today = date.today()
    my_bd = date(today.year, given_mth, given_day)
    my_bd_form = my_bd.strftime("%d.%m.%Y, %A")
    next_bd = date(today.year+1, given_mth, given_day)
    if my_bd > today:
        print(f"Twoje następne urodziny wypadają {my_bd_form}. Do urodzin pozostało {(my_bd - today).days} dni.")

    elif my_bd == today:
        print("Najlepsze życzenia! Twoje urodziny są dzisiaj!!!")

    else:
        print(f"Twoje następne urodziny wypadają {(next_bd.strftime("%d.%m.%Y, %A"))}. Do urodzin pozostało {(next_bd - today).days} dni.")

bd_alert(6, 4)

# delta to różnica. Za pomoca obiektu delta można określać różnicę między dwiema datami.


# delta
start = date.today()
difference = timedelta(days=7)
end = start + difference
print(end.strftime("%d.%m.%y"))

# datetime (z godzinami i minutami)
event = datetime.now()
print(event.hour)
print(event.minute)
print(event.strftime("%H:%M"))

# użytkownikowi trzeba podawać format w którym ma podać datę
birthday = input("Podaj date urodzenia dd.nn.rrrr: ")
d = datetime.strptime(birthday, "%d.%m.%y")