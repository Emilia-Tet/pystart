from random import choice

class Fruit:
    def __init__(self, colour, fruit_type, flavour):
        self.colour = colour
        self.fruit_type = fruit_type
        self.flavour = flavour

    def get_info(self):
        return f"It's a {self.colour}, {self.fruit_type} and {self.flavour} apple."
        

class Basket:
    def __init__(self):
        self.inside = []

    def add_fruit(self, fruit: Fruit):
        self.inside.append(fruit)


class Report:
    def get_report(self, basket, *property):
        stats = {}
        for fruit in basket.inside:
            for p in property:
                if p == 'colour':
                    stats.update({fruit.colour: stats.get(fruit.colour, 0)+1})
                if p == 'fruit_type':
                    stats.update({fruit.fruit_type: stats.get(fruit.fruit_type, 0)+1})
                if p == 'flavour':
                    stats.update({fruit.flavour: stats.get(fruit.flavour, 0)+1})

        return stats

colors = ["green", "red", "yellow"]
tastes = ["sweet", "acid"]
fruit_types = ["ripe", "unripe"]

basket = Basket()

for _ in range(100):
    apple = Fruit(choice(colors), choice(fruit_types), choice(tastes))
    print(apple.get_info())
    basket.add_fruit(apple)

report = Report()
print(report.get_report(basket, "fruit_type", "colour"))
            

