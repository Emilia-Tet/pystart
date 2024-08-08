from math import pi

class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        print("I create a new circle!")

    def count_surface(self) -> float:
        return pi*self.radius**2
    
    def circumference(self) -> float:
        return 2*pi*self.radius
    
def test_circle_calculations():
    circle = Circle(5)
    field = circle.count_surface()
    circumference = circle.circumference()

    assert 78.5 < field < 78.6
    assert 31.4 < circumference < 31.5

if __name__ == '__main__':
    radius1 = 10

    circle1 = circle1 = Circle(radius1)
    surf1 = circle1.count_surface()
    circum1 = circle1.circumference()
    print(surf1, circum1)
