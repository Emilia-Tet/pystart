from zadanie1 import group_them

def test_group_them_empty():
    assert group_them() == ''


def test_group_them_two():
    assert group_them(python='super', java='almost super') == 'Python is super\nJava is almost super'

def test_group_them_one():
    assert group_them(python='super') == 'Python is super'
