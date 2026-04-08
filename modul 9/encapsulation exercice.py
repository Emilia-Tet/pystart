# program przechowuje liste zakupow
# kazdy obiekt jest osobnym obiektem klasy ListItem
# produkty do zakupienia w zmiennej prywatnej
# dany produkt jest na liscie raz, najwyzej zwieksza sie jego ilosc
# metody:
# addItem(product: Product, quantity: float)
# removeItem(product: Product, quantity: float)
# listItems
# calculateTotalCost
# kazdy obiekt klasy Product posiada cene oraz nazwe
# koszyk odpowiada za informacje o ilosci, ale pojedynczy wiersz takze bedzie klasa

class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class Basket_row:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity
    
    def add_item(self, added_quantity):
        self.quantity = self.quantity+added_quantity
    
    def remove_item(self, removed_quantity):
        if result:=(self.quantity-removed_quantity) >= 0:
            self.quantity = result
        else:
           print("Nie mozesz usunac wiecej produktow, niz tam masz")

    def calculate_cost_per_product(self):
        return self.quantity*self.product.__price

butter = Product("maslo", "10")
butter_row = Basket_row(butter, 3)
total_price = butter_row.calculate_cost_per_product()

print(total_price)