from json import dump, load
from datetime import date

# plik powinien zawierać puste klamerki []



def add_new_expense():
    category = input('Czego dotyczy wydatek? ')
    amount = float(input('Dodaj wydatek: '))
    today = date.today()

    with open('wydatki.json') as file:
        expenses = load(file)

    with open('wydatki.json', 'w') as file:
        expenses.append({
            'amount': amount,
            'category': category,
            'date': today.strftime(('%d.%m.%Y, %A'))
        })
        dump(expenses, file)

def print_all_expenses():
    with open('wydatki.json') as file:
        expenses = load(file)

    total_amount = 0
    for e in expenses:
        amount = e.get('amount')
        print('Kwota', amount)
        total_amount += amount
        print('Kategoria', e.get('category'))
        print('Data', e.get('date'))
        print('--'*10)
    print(f'TOTAL: {total_amount:.2f}')


def main():
    decision = input('Co chcesz zrobić? [d] dodaj wydatek, [w] wypisz wszystkie.')
    if decision == 'd':
        add_new_expense()
    elif decision == 'w':
        print_all_expenses()
    else:
        print('Wybierz [d] aby dodać wydatek, lub [w] żeby wczytać dotąd zarejestrowane wydatki i ich sumę.')

if __name__ == '__main__':
    main()
    
