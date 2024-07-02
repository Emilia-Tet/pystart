# dobry test ma 3 części: given, when, then
import pytest
from pystart_package.utils import lists

list1 = [45,7]
lis2 = [76, 32, 1, 67]
print(lists.add_lists(list1, lis2))

def add_numbers(int1, int2) -> int:
    return int1 + int2


def test_add_numbers():
    # given
    int1 = 3
    int2 = 2

    #when
    value = add_numbers(int1, int2)

    assert value == 5