# Nie można używać .2f bez format() albo f-stringa. 
# format działa identycznie jak f-string, tylko składnia jest trochę starsza

from requests import get

waluty_url = "https://api.nbp.pl/api/exchangerates/tables/C/"
wynik = get(waluty_url)
waluty = wynik.json()
# print(waluty[0]['rates'])

kwota = 1000

for waluta in waluty[0]['rates']:
    nazwa = waluta['currency']
    cena_kupna = waluta['bid']
    wynik_przeliczenia = kwota / cena_kupna
    print('To będzie {:.2f} w walucie: {}'.format(wynik_przeliczenia, nazwa))