# brutto -> netto
stawka_vat = float(input('Podaj mi stawkę VAT, np "23": '))
kwota_brutto = float(input('Podaj mi kwotę brutto: '))

kwota_netto = kwota_brutto / 1.23
print('Do zapłaty kwota netto: ', format(kwota_netto, '2f'))