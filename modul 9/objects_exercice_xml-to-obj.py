# jeżeli utworzymy klase Author, to potem tworząc klase Book możemy wpisać data type argumentu author: Author
# kiedy obiekty łączą się ze sobą, zdecydowanie gdzie będzie przynależeć dana metoda, nie jest oczywiste
from datetime import date

class Author:
    def __init__(self, f_name: str, l_name: str, birthdate: date):
        self.f_name = f_name
        self.l_name = l_name
        self.birthdate = birthdate


class Book:
    def __init__(self, title: str, description: str, excerpt: str, rating: int):
        self.description = description
        self.excerpt = excerpt
        self.rating = rating
        self.title = title
        self.authors = []

    def add_author(self, author: Author):
        self.authors.append(author)

author1 = Author(f_name="Bonifacy", l_name="Smith", birthdate=date(1910, 10, 10))
author2 = Author("John", "Smith", date(1905, 5, 15))

book1 = Book('A', 'Kryminał', '...', 5)
book1.add_author(author1)
book1.add_author(author2)

print(book1)

print(book1.authors[0].birthdate)

                 


