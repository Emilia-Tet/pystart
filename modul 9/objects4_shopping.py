import sqlite3
from random import choice, randint

def create_table():
    with sqlite3.connect("basket.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Transactions (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                OrderNumber INTEGER,
                ProductName TEXT,
                Quantity INTEGER,
                TotalPrice REAL
            )
        """)
        conn.commit()

create_table()

def get_next_order_number():
    with sqlite3.connect("basket.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(OrderNumber) FROM Transactions")
        result = cursor.fetchone()
        if result[0] is None:  # Jeśli tabela jest pusta
            return 1
        return result[0] + 1

class Product:
    def __init__(self, name, price: float):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Cena musi być liczbą dodatnią")
        self.name = name
        self.price = price

class Basket_row:
    def __init__(self, product_in_row: Product, quantity: int):
        self.product_in_row = product_in_row
        self.quantity = quantity

    def calculate_cost_per_product(self):
        return self.quantity*self.product_in_row.price
    
class Basket:
    def __init__(self):
        self.rows = []

    def add_item(self, product_to_add: Product, quantity):
        if quantity <= 0:
            raise ValueError("Dodawana ilość musi być większa od 0")
        for row in self.rows:
            if row.product_in_row.name == product_to_add.name:
                row.quantity += quantity
                return
        self.rows.append(Basket_row(product_to_add, quantity))

    def remove_item(self, product: Product, quantity):
        if quantity <= 0:
            raise ValueError("Usuwana ilość musi być większa od 0")
        for row in self.rows:
            if row.product_in_row.name == product.name:
                if quantity > row.quantity:
                    raise ValueError("Nie możesz usunąć więcej produktów, niż jest w koszyku")
                row.quantity -= quantity
                if row.quantity == 0:
                    self.rows.remove(row)
                    return
                else:
                    return
        raise Exception('Nie możesz usunąc produktu, którego tam nie ma')
        
    def list_items(self):
        return [f'name: {r.product_in_row.name}, quantity: {r.quantity}, price: {r.calculate_cost_per_product()}' for r in self.rows]

    def calculate_total_cost(self):
        return sum(map(lambda obj: obj.calculate_cost_per_product(), self.rows))
    
    def save_basket_to_db(self):
        with sqlite3.connect("basket.db") as conn:
            cursor = conn.cursor()
            transaction_id = get_next_order_number()
            for row in self.rows:
                cursor.execute("""
                    INSERT INTO Transactions (OrderNumber, ProductName, Quantity, TotalPrice)
                    VALUES (?, ?, ?, ?)
                """, (transaction_id, row.product_in_row.name, row.quantity, row.calculate_cost_per_product()))
            
        
        conn.commit()
        conn.close()
        print(f"Zamówienie nr {transaction_id} zapisano do bazy danych!")
    
butter = Product('masło', 8)
bread = Product('chleb', 5)
ham = Product('szynka', 10)
tomato = Product('pomidor', 2)
chocolate = Product('czekolada', 6)
pepper = Product('papryka', 4)
salad = Product('sałata', 7)
onion = Product('cebula', 1)

products = [
    butter,
    bread,
    ham,
    tomato,
    chocolate,
    pepper,
    salad,
    onion]

cart = Basket()
cart.list_items()
cart.calculate_total_cost()

cart.add_item(bread, 3)
cart.add_item(butter, 2)
cart.add_item(ham, 2)

cart.list_items()
cart.calculate_total_cost()

cart.remove_item(ham, 1)
cart.list_items()
cart.calculate_total_cost()

cart.add_item(bread, 3)
cart.list_items()
cart.calculate_total_cost()

cart.remove_item(ham, 1)
cart.list_items()
cart.calculate_total_cost()

# cart.remove_item(ham, 1)
# cart.remove_item(bread, 7)objects
# cart.remove_item(bread, 0)

cart.save_basket_to_db()

for i in range(50):
    cart = Basket()
    for j in range(randint(1,5)):
        cart.add_item(choice(products), randint(1,15))
    cart.save_basket_to_db()
