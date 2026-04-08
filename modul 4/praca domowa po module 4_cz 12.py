print("Podaj liste slow oddzielona przecinkami: ")
input_str = input("").split(sep=",")

print("\n".join(set(input_str)))

#albo

sentence = "ale, dzisiaj, pada, i, pada"
words = set()

for word in sentence.split(","):
    words.add(word.strip())

for word in words:
    print(word)

