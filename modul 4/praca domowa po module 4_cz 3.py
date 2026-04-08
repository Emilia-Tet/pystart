example = "Ala ma kota"

def caesar_cipher(text, num) -> str:
    text = text.lower()
    Alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for char in range(0, len(text)):
        if text[char] == ' ':
            continue
        position = Alphabet.index(text[char])
        text = text.replace(text[char], Alphabet[position+num], 1)
    return text

def decode_caesar(text, password) -> str:
    text = text.lower()
    Alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    for char in range(0, len(text)):
        if text[char] == ' ':
            continue
        position = Alphabet.index(text[char])
        text = text.replace(text[char], Alphabet[position-password], 1)
    return text

print(caesar_cipher(example, 3))
print(caesar_cipher("zuzu", 3))
print(decode_caesar("drd pd nowd", 3))
# ord
# chr

# Kacepr zmienia wszystko na upper
# Kacper uzyl %27 zebyz dowolnej liczby znalezc pozycje
SECRET = 3
text_print = input("Podaj mi tekst do przetworzenia: ")
action = input('1. Odszyfruj, 2. Zaszyfruj')
text_print = text_print.upper()

encrypted_text = ''
for char in text_print:
    if char.isalpha():
        if action == '1':
            char = chr((ord(char) - SECRET - ord('A')) % 26 + ord('A'))
        elif action == '2':
            char = chr((ord(char) + SECRET - ord('A')) % 26 + ord('A'))
    encrypted_text += char
print(encrypted_text)


# jeszcze propozycja Leszka:
# shift = 97 if char.islower() else 65