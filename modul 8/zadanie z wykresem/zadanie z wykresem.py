from datetime import datetime
import matplotlib.pyplot as plt

dict_total_income = {}
dict_transactions = {}

with open('zadanie z wykresem\operacje.csv', 'r', encoding='utf-8-sig') as input_file:
    # pomija 1 linię
    next(input_file)
    for line in input_file:
        strdate, category, description, amount = line.split(sep=',')
        amount = float(amount.strip())
        print(strdate)
        daily_date = datetime.strptime(strdate, '%Y-%m-%d')
        month = daily_date.strftime('%B')
        print(month)
        if category =='przychód':
            dict_total_income[month] = dict_total_income.get(month, 0) + amount
        dict_transactions[month] = dict_transactions.get(month, 0) + 1
    print(dict_total_income)
    print(dict_transactions)

figure, axes = plt.subplots(2, 1)
# 2 wiersze (1 kolumna), więc wykresy będą jeden nad drugim
months = dict_total_income.keys()
amounts = dict_total_income.values()
axes[0].set_xlabel('Miesiące')
axes[0].set(ylabel='Kwoty', title='Suma przychodów')
axes[0].bar(months, amounts)

months2 = dict_transactions.keys()
transactions = dict_transactions.values()
axes[1].set_xlabel('Miesiące')
axes[1].set(ylabel='Ilość transakcji', title='Ilość transakcji w miesiącu')
axes[1].bar(months2, transactions)


plt.tight_layout()
plt.show()


