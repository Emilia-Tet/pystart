import re

def remove_punctuation(text):
    # Definiowanie wzorca dla znaków interpunkcyjnych
    pattern = r'[^\w\s]'
    # Zamiana znaków interpunkcyjnych na pusty ciąg
    clean_text = re.sub(pattern, '', text)
    return clean_text

def count_word(input_text, keyword, chars_type = False):
    counter = 0
    for word in input_text.split(" "):
        if chars_type:
            if remove_punctuation(word) == keyword:
                counter += 1

        else:
            if remove_punctuation(word.lower()) == keyword.lower():
                counter += 1
    return counter


def test_count_word_no_type_char():
    assert count_word("Python i Python", "Python") == 2
    assert count_word("Dlaczego koty, koty i koty!", "koty") == 3
    assert count_word("Dlaczego koty, koty i koty!", "pies") == 0
    assert count_word("Pieniądze i pieniądze, nie tylko o to chodzi...", "pieniądze") == 2


def test_count_word_true_type_char():
    assert count_word("Python i python", "Python", chars_type=True) == 1
    assert count_word("Dlaczego koty, Koty i koty!", "koty", chars_type=True) == 2
    assert count_word("Dlaczego koty, koty i koty!", "Koty", chars_type=True) == 0
    assert count_word("Pieniądze i pieniądze, nie tylko o to chodzi...", "pieniądze", chars_type=True) == 1


    