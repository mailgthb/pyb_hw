"""
Zadanie 4: uporyadochennaya podstroka.
USLOVIE:
Postroit' funkcional kotoryj budet nahodit' v stroke podstroku maksimal'noj dliny,
 v kotoroj bukvy uporyadocheny v alfavitnom poryadke.
VHOD: stroka
VYHOD: podstroka
Primer:
s = "sabrrtuwacaddabra"
...
> "abrrtuw"
"""

ABETKA = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'"
ABC = "abcdefghijklmnopqrstuvwxyz"

line = input("Введіть текстовий рядок (без пробілів, "
             "розділових знаків, інших символів, "
             "лише букви української/англійської мови та апостроф): ").lower()
enorua = input("Українська(1) чи англійська(2)? ")
longest_ordered_substring = ''

num_pos = -1
longest_ordered_substring_result = ''

if enorua == '2':
    ABETKA = ABC

for letter in line:
    num_pos_prev = num_pos
    num_pos = ABETKA.index(letter)
    if num_pos >= num_pos_prev:
        longest_ordered_substring += letter
    else:
        if len(longest_ordered_substring) > len(longest_ordered_substring_result):
            longest_ordered_substring_result = longest_ordered_substring
        longest_ordered_substring = letter
print("Підрядок максимальної довжини, в якому літери впорядковані \
    в алфавітному порядку є: ", longest_ordered_substring_result)  
    

