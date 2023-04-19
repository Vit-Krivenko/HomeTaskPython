phrase = "пара-ра-рам рам-пам-папам па-ра-па-да"
words = phrase.split()
list_1 = list(map(lambda word: sum(1 for letter in word if letter in "ёуеыаоэяию"), words))
list_2 = set(list_1)
if len(list_2) == 1:
   print("Парам пам-пам")
else:
   print("Пам парам") 