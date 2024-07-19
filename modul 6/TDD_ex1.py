# 1. Najpierw piszę funkcję ale bez treści tylko pass
# 2. od razu tworzę test na jeden scenariusz (że nwd istnieje) i daję dość oczywiste dane
# 3. uruchamiam pythom -m pytest
# 4. piszę funkcję i wychodzi mi, że potrzebuję innej funkcji w środku
# 5. najpierw piszę test tej funkcji, potem samą funkcję
# 6. na koniec uruchamian testy

from math import ceil

def get_divisors(number: int) -> set:
    divisors = set()
    for test_divisor in range(2, ceil(number / 2)+1): #musi być plus 1, bo np 12/2 to jest 6, a musi być iwęcej niż 1/2
        if number % test_divisor == 0:
            divisors.add(test_divisor)
    divisors.add(number)
    return divisors




def gcd(number1 : int, number2 : int) -> int:
    divisors1 = get_divisors(number1)
    divisors2 = get_divisors(number2)
    common_divisors = divisors1 & divisors2
    return max(common_divisors) if len(common_divisors) > 0 else None

def test_gcd_exists():
    assert gcd(20, 30) == 10
    assert gcd(15, 30) == 15

def test_gcd_doesnt_exist():
    assert gcd(7, 30) is None

def test_get_divisors():
    assert get_divisors(6) == {2, 3, 6}
