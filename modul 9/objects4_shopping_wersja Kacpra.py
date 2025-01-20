# podkreślenie przy _find product mówi, że jest to meoda wewnętrzna

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class List_item:
    def __init__(self, product: Product, quantity: float):
        self.product = product
        self.quantity = quantity


class Cart_List:
    def __init__(self,):
        self._items = []

    def add_item(self, product: Product, quantity: float):
        pos = self._find_product(product)
        if pos is None:
            self._items.append(
                List_item(product, quantity)
            )
        else:
            self._items[pos].quantity += quantity

            if self._items[pos].quantity == 0:
                del self._items[pos]

    def remove_item(self, product: Product, quantity: float):
        pos = self._find_product(product)
        if pos is None:
            self.items.append(
                List_item(product, quantity)
            )
        else:
            self._items[pos].quantity -= quantity

            if self._items[pos].quantity == 0:
                del self._items[pos]

    def _find_product(self, product: Product):
        for pos, item in enumerate(self._items):
            if item.product.name == product.name:
                return pos
        return None


    def list_items(self) -> list:
        return self._items

    def calculate_total_cost(self) -> float:
        total = 0
        for item in self._items:
            total += item.quantity * item.product.price
        return total
    

def test_check_total_cost():
    bread = Product('chleb', 6.5)
    ham = Product('szynka', 80)
    butter = Product('masło', 8)

    cart = Cart_List()
    cart.add_item(bread, 2)
    cart.add_item(bread, 2)
    cart.add_item(ham, 0.5)
    cart.add_item(butter, 2)

    assert len(cart.list_items()) == 3
    assert cart.calculate_total_cost() == 4*6.5 +40 +16

    cart.remove_item(bread, 2)
    assert len(cart.list_items()) == 3
    assert cart.calculate_total_cost() == 2*6.5 +40 +16

    cart.remove_item(bread, 2)
    assert len(cart.list_items()) == 2
    assert cart.calculate_total_cost() == 40 +16
