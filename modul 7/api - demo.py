from requests import get

url = 'http://api.nbp.pl/api/exchangerates/tables/A/'
codes = ['EUR', 'USD', 'GBP']
response = get(url)
data = response.json()
for rate in data[0]['rates']:
    if rate['code'] in codes:
        print(rate['currency'], rate['mid'])