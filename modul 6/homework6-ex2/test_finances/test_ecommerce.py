from finances.ecommerce import calculate_brutto, calculate_netto, calculate_discount
# cd test_projekt
# cd .. przeniesie mnie o piętro wyżej

def test_calculate_brutto():
    assert calculate_brutto(100) == 123.0
    assert calculate_brutto(100, 0.05) == 105.0

def test_calculate_netto():
    assert calculate_netto(123) == 100.0
    assert calculate_netto(105, 0.05) == 100.0

def test_calculate_discount():
    assert calculate_discount(100, []) == 100
    assert calculate_discount(100, [0.1]) == 90
    assert calculate_discount(100, [0.1, 0.1]) == 81
