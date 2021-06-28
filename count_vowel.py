import colorama
from colorama import Fore, Back, Style
colorama.init()

VOWELS = "уеіїаоєяию"

line = input("Наберіть текстовий рядок: ")
num_vowels = 0
for vowel in VOWELS:
    for symb in line:
        if vowel == symb:
            num_vowels += 1
print(num_vowels)


