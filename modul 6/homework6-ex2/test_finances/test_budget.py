from finances.budget import calculate_expenses
from finances.budget import calculate_monthly_budget
# -vvv to komenda żeby pytest więcej opisał co zrobił, daje się na końcu linii dodatkowo 


def test_calculate_expenses():
    assert calculate_expenses([100, 200]) == 300

def test_calculate_monthly_budget():
    assert calculate_monthly_budget(200, 100) == 100
