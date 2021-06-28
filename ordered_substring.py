import colorama
from colorama import Fore, Back, Style
colorama.init()
ABETKA = "абвгґдеєжзиіїйклмнопрстуфхцчшщюяь"

# Дивлюсь я на небо і думку гадаю
line = input("Введіть текстовий рядок: ").lower()
longest_ordered_substring = ''
num_pos = -1
list_str = []

for letter in line:
    print(F"letter = {letter}")
    
    if letter == ' ':
        #longest_ordered_substring += ' '
        list_str.append(longest_ordered_substring)
        longest_ordered_substring = ''
        continue
    
    num_pos_prev = num_pos
    print(F"num_pos_prev = num_pos = {num_pos}")
    
    num_pos = ABETKA.index(letter)
    if num_pos >= num_pos_prev:
        longest_ordered_substring += letter
    else:
        list_str.append(longest_ordered_substring)
        longest_ordered_substring = letter
print(list_str)  
    
    
