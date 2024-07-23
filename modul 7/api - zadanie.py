from requests import get


url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = get(url)
data = response.json()
codes = ['temperatura', 'cisnienie']
for synop_dict in data:
    if synop_dict['stacja'] == 'Warszawa':
        print(synop_dict['temperatura'], synop_dict['cisnienie'])
        break

