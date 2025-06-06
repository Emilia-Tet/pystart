from datetime import datetime, date
today = datetime.now()
# today = date.today()
# parsed_today = today.strftime(r'%d.%m.%Y')

class BaseEmployee():
    def __init__(self, f_name, l_name, emplo_date):
        self.f_name = f_name
        self.l_name = l_name
        self.emplo_date = emplo_date
        self.emplo_date = datetime.strptime(emplo_date, r'%d.%m.%Y')
        today = datetime.now()

        age = (today - self.emplo_date).days / 365.25

        if age >= 50:
            raise ValueError('Okres zatrudnienia przekracza 50 lat.')
        
        if self.emplo_date > today:
            raise ValueError('Data zatrudnienia nie moze byc w przyszlosci.')
        
        #InvalidDateOfEmployment()

    def get_employment_time(self):
        return (today - self.emplo_date).days


emplo1 = BaseEmployee('Jan', 'Kowalski', '01.01.2025')
emplo2 = BaseEmployee('Ola', 'Ola', '01.02.2028')
emplo3 = BaseEmployee('Ola', 'Ola', '01.02.1901')

emplo1.get_employment_time()

class Employee(BaseEmployee):
    def __init__(self, f_name, l_name, emplo_date, hourly_rate, work_type, bonus):
        super().__init__(f_name, l_name, emplo_date)
        self.hourly_rate = hourly_rate
        self.work_type = work_type
        self.bonus = bonus

    def calculate_salary(self):
        return self.hourly_rate * self.work_type + self.bonus
    


################## wersja Kacpra #################
from datetime import date, datetime

class InvalidDateOfEmployment(Exception):
    pass

class BaseEmployee():
    def __init__(self, first_name: str, last_name: str, employment_date: date):
        today = datetime.today().date()
        employment_time = today.year - employment_date.year

        self.first_name = first_name
        self.last_name = last_name
        self.employment_date = employment_date

        if employment_date > today or employment_time > 50:
            raise InvalidDateOfEmployment('Data zatrudnienia jest nieprawidlowa')
        
    def __lt__(self, other: BaseEmployee):
        return self.employment_date < other.employment_date
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_employment_time(self):
        today = datetime.today().date()
        employment_time = today - self.employment_date

        return employment_time.days
    
        
empl_error_test = BaseEmployee('A', 'B', date(2025, 11, 12))
empl_error_test_2 = BaseEmployee('A', 'B', date(1902, 11, 12))

empl1 = BaseEmployee('A', 'B', date(2000, 11, 12))
empl2= BaseEmployee('C', 'D', date(1998, 11, 12))
empl3= BaseEmployee('E', 'F', date(1996, 11, 12))

employees = [empl1, empl2, empl3]
employees.sort()
employees.sort(reverse=True)
print(employees)

empl1.get_employment_time()

class Employee(BaseEmployee):
    def __init__(self, 
                 first_name, 
                 last_name, 
                 employment_date: date, 
                 hourly_rate: float, 
                 number_of_hours: int, 
                 bonus: int = 0):
        super().__init__(first_name, last_name, employment_date)
        self.hourly_rate = hourly_rate
        self.number_of_hours = number_of_hours
        self.bonus = bonus


    def get_salary(self):
        return self.hourly_rate * self.number_of_hours + self.bonus
