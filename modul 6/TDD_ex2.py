# testuję różne aspekty: czy zwraca listę tak jak miało, czy zwraca wartości graniczne.
# pisząc range nie mogę potraktować tego divisora jako step: return list(range(range_start, range_end, divisor)) ponieważ step zabierze pierwszy element z listy


def return_numbers(range_start:int, range_end:int, divisor:int) -> list:
        return [num for num in range(range_start, range_end+1) if num%divisor == 0]


def test_return_numbers():
    assert return_numbers(3, 15, 2) == [4, 6, 8, 10, 12, 14]
    assert return_numbers(1, 12, 40) == []
    assert return_numbers(2, 10, 2) == [2, 4, 6, 8, 10]

def test_return_numbers_returns_list():
      assert isinstance(return_numbers(2, 15, 3), list)
