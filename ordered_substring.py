import colorama
from colorama import Fore, Back, Style
colorama.init()

ABETKA = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'"

line = input("Введіть текстовий рядок (без пробілів, "
             "розділових знаків, інших символів, "
             "лише букви української мови та апостроф): ").lower()
longest_ordered_substring = ''
num_pos = -1
longest_ordered_substring_result = ''

for letter in line:
    num_pos_prev = num_pos
    num_pos = ABETKA.index(letter)
    if num_pos >= num_pos_prev:
        longest_ordered_substring += letter
    else:
        if len(longest_ordered_substring) > len(longest_ordered_substring_result):
            longest_ordered_substring_result = longest_ordered_substring
        longest_ordered_substring = letter
print("Підрядок максимальної довжини, в якому літери впорядковані в алфавітному порядку є: ", longest_ordered_substring_result)  
    
    
