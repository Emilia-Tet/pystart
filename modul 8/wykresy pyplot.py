import matplotlib.pyplot as plt

figure, axes = plt.subplots()
cities = ['Gdynia', 'Gdańsk', 'Sopot']
people = [220, 250, 300]

axes.set_xlabel('Miasta')
axes.set(ylabel='Ilość komentarzy', title='Ilość dodanych komentarzy')

axes.bar(cities, people)
plt.show()
plt.savefig('testowy_wykres.jpg')
