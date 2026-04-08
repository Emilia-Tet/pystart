# kiedy iteruje po 2 kolekcjach naraz
list1 = [5,6,8,3,9,10]
list2 = ['a', 'b', 'c', 'd']

# zwraca cos inneog niz liste, trzeba dopiero ja zrobic
# jak dam nierowne ilosci, to wyrowna tylko do krotszej a dluzsza liste pominie
print(list(zip(list1, list2)))

# mozna iterowac po tym co zwraca zip bez mzinay na liste

f_names = ["Zofia", "Leopold", "Gabriela"]
l_names = ['Nalkowska', 'Staff', 'Zapolska']

for fname, lname in zip(f_names, l_names):
    print(f"Imie {fname}, nazwisko {lname}.")

# mozna zipowac wiecej niz 2 argumenty
print(list(zip(list1, f_names, l_names, list2)))