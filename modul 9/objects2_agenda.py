from json import dump, load, JSONDecodeError
from datetime import datetime, timedelta
import os

# date przechowuje tylko datę (rok, miesiąc, dzień), a datetime przechowuje zarówno datę, jak i czas (rok, miesiąc, dzień, godzina, minuta, sekunda). 
# teraz = datetime.now()
# dzisiaj = date.today()
# metoda .date() z obiektu datetime pobiera samą datę dzienną.

# strptime (parse time) jest używana do konwersji ciągu znaków (str) na obiekt datetime. Jest funkcją.
# strftime (format time) jest używana do konwersji obiektu datetime na ciąg znaków (str). Jest metodą.

# ja się zatrzymałam na tym, jak to zrobić żeby sie spotkania nie pokrywały. Kacper proponuje, żeby data była kluczem.
# faktycznie mozna sprwdzić czy start nowego eventu nie jest pomiędzy start i end istniejącego eventu


class Calendar:

    def add_meeting(self, meeting):
        if not os.path.exists('meetings.json'):
            with open('meetings.json', 'w') as file:
                dump([], file)

        with open('meetings.json', 'r') as file:
            try:
                meetings = load(file)
            except JSONDecodeError:
                meetings = []

            meetings.append({
            'title': meeting.title,
            'start_date': meeting.start_date.strftime("%d.%m.%Y %H:%M"),
            'end_date': meeting.end_date.strftime("%d.%m.%Y %H:%M")
        })
        with open('meetings.json', 'w') as file:
            dump(meetings, file)

    def display_calendar(self, day=None):
        with open('meetings.json', 'r') as file:
            try:
                meetings = load(file)

            except JSONDecodeError:
                meetings = []

        if day is None:
            return meetings
        
        events = []
        for event in meetings:
            event_date = datetime.strptime(event['start_date'], "%d.%m.%Y %H:%M")
            if event_date.date() == datetime.strptime(day, "%d.%m.%Y"):
                events.append(event)
        return events


    def check_date(self, event_at: datetime):
        with open('meetings.json', 'r') as file:
            try:
                meetings = load(file)
            except JSONDecodeError:
                meetings = []
                
        for meeting in meetings:
            start_date = datetime.strptime(meeting['start_date'], "%d.%m.%Y %H:%M")
            end_date = datetime.strptime(meeting['end_date'], "%d.%m.%Y %H:%M")
            if start_date <= event_at < end_date:
                return False
        return True
        


class Meeting:
    def __init__(self, title: str, date_str: str):
        self.title = title
        self.start_date = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
        self.end_date = self.start_date + timedelta(minutes=60)


meeting1 = Meeting("spotkanie z Gosią", "13.08.2024 14:15")
my_calendar = Calendar()

if my_calendar.check_date(meeting1.start_date):
    my_calendar.add_meeting(meeting1)
else:
    print("Ten termin jest juz zajety")

print(my_calendar.display_calendar("13.08.2024"))