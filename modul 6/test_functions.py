# nie musze imortować pystest na górze
# żeby uruchomić test, wpisuję w terminal pytest i nazwę pliku
# Kacper napisał python -m pytest nazwa_pliku.py
# Użycie python -m oznacza, że pytest jest uruchamiany jako moduł w kontekście konfiguracji Pythona, co może obejmować specyficzne ustawienia dla Twojej instalacji Pythona.
# python -m pytest automatycznie ustawia ścieżkę modułów, co może pomóc w uniknięciu problemów z importem, zwłaszcza w bardziej złożonych projektach, gdzie struktura katalogów może być skomplikowana.
# plik powinien nazywać się od test_ i funkcja testująca także, plus powinnna mieć assert (spodziewana wartość)

def add_numbers(int1, int2) -> int:
    return int1 + int2


def test_add_numbers():
    # given
    int1 = 3
    int2 = 2

    #when
    value = add_numbers(int1, int2)

    assert value == 5
    assert value == 8

