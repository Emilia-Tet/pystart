from math import pi


def circle_area(r: float) -> float:
    return pi * r ** 2


def circle_circumference(r: float) -> float:
    return 2 * pi * r


def equilateral_triangle_circumference(a: float) -> float:
    return 3*a


def equilateral_triangle_area(a: float) -> float:
    return (a**2 * 3**0.5)/4
