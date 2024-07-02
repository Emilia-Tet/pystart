def count_chars_between(text:str, char_start:str='(', char_end:str=')'):
                        
    should_i_count = False
    counter = 0

    for char in text:
        if char == char_end:
            should_i_count = False

        if should_i_count:
            counter +=1

        if char == char_start:
            should_i_count = True

    return counter


def test_count_chars_between_round_brackets():
    assert count_chars_between("lubię koty (ale nie wszystkie)") == 17

def test_count_chars_between_triangle_brackets():
    assert count_chars_between("nie lubię węży <ale lubię Pythona>", "<", ">") == 17

def test_count_chars_between_no_brackets():
    assert count_chars_between("tutaj nie ma żadnych nawiasów") == 0


    




