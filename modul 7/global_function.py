# global pomaga, jeśli nie zna się obiektów

# zmienna c jest zmienną globalną i jest dostępna w funkcji
# aby móc ją modyfikować, musimy użyć słowa kluczowego "global"
# po wywołaniu funkcji, wartość zmiennej x zostanie zmieniona na 10 i będzie dostępna poza funkcją

def sum_it(a, b):
    global c
    c = 10
    return a + b + c

global c
c = 20
print(c)

# po wywołaniu funkcji z global c, c będzie miało ogólnie inną wartość
print(sum_it(4, 5))
print(c)

