# Sukurkite programą, kuri iš sakinių, kuriuos jus įvedėt, sukurtų dict, kuriame keys reikštų raides,
# o values šių raidžių dažnumą tuose sakiniuose. Programa turi reikalauti,
# kad vartotojas įvestų ne mažiau kaip 3 sakinius.

char_dictionary = {}
for y in range(3):
    sentence = input('Enter your sentence: ')

    for x in sentence:
        if x in char_dictionary:
            char_dictionary[x] += 1
        else:
            char_dictionary[x] = 1
print(char_dictionary)

