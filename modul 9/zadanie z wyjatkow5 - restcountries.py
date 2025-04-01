# ważne, żeby w przypadku braku dostępu do internetu program nie scrashował zupełnie, ale nadal działał

from requests import get, exceptions
from json import load, dump

def get_capital(check_country: str):
    print(f'Sprawdzam stolicę dla państwa {check_country}')
    url = f'https://restcountries.com/v3.1/name/{check_country.lower()}'
    response = get(url)
    # print(response.json())
    output = response.json()[0]
    return output['capital'][0]

def load_capitals():
    try:
        with open('capitals.json') as file:
            capitals = load(file)
    except FileNotFoundError:
        capitals = {}
    return capitals

capitals = load_capitals()
country = input('Podaj nazwę kraju: ')


try: 
    if country not in capitals:
        capital = get_capital(country)
    else:
        capital = capitals[country]
    print(capital)


    capitals[country] =  capital
    with open('capitals.json', mode='w') as file:
        dump(capitals, file)

except exceptions.ConnectionError:
    print('Wystąpił problem z połączeniem.')

except KeyError:
    print('Nie mam tego kraju na liście.')

# można wrzucić do json formattera to będzie czytelniej
# print(json.dumps(response.json(), indent=4, ensure_ascii=False))