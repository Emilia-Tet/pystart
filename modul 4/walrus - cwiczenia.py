
lista = []
while (i:= int(input("Podaj liczbe inna niz 0: "))) != 0:
    lista.append(i)

for i in lista:
    print(i)
print(f"Srednia to {sum(lista)/len(lista)}")

