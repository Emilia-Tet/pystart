# MVC: Model, View, Controller
# Django: MVT: Model, View, Template
# View - HTML/CSS/JS dla stron, a dla intefejsow: klasy konfigurujące guziki itd.
# Model: odwzorowuje model danych, bazy pod spodem, logikę biznesową. Klasy mapujące wiersze z bazy do obiektów. ORM: object related maper, np SQL Alchemy.

# Controller odbiera żądania od użytkownika, pilnuje uprawnień i poprawności danych i zapytań, poprzez model komunikuje sie z bazą i przygotowuje odpowiedzi 

# def eq_sum_powdig(h_max, exp: int):
#     result = []
#     exceptions = [0,1]
#     for i in range(0,h_max+1):
#         number = 0
#         for n in str(i):
#             number += int(n)**int(exp)
#         if number == int(i) and number not in exceptions:
#             result.append(int(i))
#     return result

# eq_sum_powdig(153, 3)