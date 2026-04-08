from datetime import date
#iso format najlepszy do baz danych
# wiecej formatow na stronie https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
# p jak parsowanie (strptime)

today = date.today()
print(f"Today is {today}")

formatted_today = today.strftime("%d.%m.%Y")
# strf = string formatted
print(f"Today is {formatted_today}")

day = date(today.year, 11, 9)