import colorama
from colorama import Fore, Back, Style
colorama.init()

VOWELS = "уеіїаоєяию"

line = input("Наберіть текстовий рядок: ").lower()
num_vowels = 0
for symb in line:
    if symb in VOWELS:
        num_vowels += 1
print(num_vowels)