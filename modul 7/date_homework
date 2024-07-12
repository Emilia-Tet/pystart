from datetime import datetime, date, timedelta
dai_salary = 200
start_date = "01.07.2024"
end_date = "10.07.2024"

def calculate_salary(st_time, en_time, daily_salary):
    parsed_st = datetime.strptime(st_time, "%d.%m.%Y")
    parsed_en = datetime.strptime(en_time, "%d.%m.%Y")
    working_time = parsed_en - parsed_st

    working_days = working_time.days+1

    day_to_print = date(parsed_st.year, parsed_st.month, parsed_st.day)
    for _ in range(working_days+1):
        print(day_to_print, week_day := day_to_print.strftime("%A"))
        if week_day == "Saturday" or week_day == "Sunday":
        # lepiej: if week_day in ["Saturday", "Sunday"]:
            working_days += 1
        day_to_print = date(day_to_print.year, day_to_print.month, day_to_print.day+1)

    return daily_salary * working_days

print(calculate_salary(start_date, end_date, dai_salary))

# wersja Kacpra

date_start = datetime.strptime(input("Podaj datę rozpoczęcia dd.mm.rrrr"), "%d.%m.%Y")
date_end = datetime.strptime(input("Podaj datę zakończenia dd.mm.rrrr"), "%d.%m.%Y")
rate = float(input("Podaj dzienną stawkę: "))

diff = date_end - date_start
salary = (diff.days + 1) * rate

while date_start <= date_end:
    if date_start.strftime("%a") in ['Sat', 'Sun']:
        salary += rate
        print(date_start.strftime("%a %d.%m.%Y"))
        date_start += timedelta(days=1)
