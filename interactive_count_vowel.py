"""
Написать программу (python script), которая при запуске будет запрашивать пользователя ввести произвольную строку и выдавать в ответе количество гласных букв.
Примечание:
- для ручного ввода используем встроенную функцию raw_input();
- для простоты на вход принимаем строку из букв латинского алфавита;
- набор гласных принимаем за 'a', 'e', 'i', 'o', 'u';
- программа должна быть нечувствительна к регистру.
ВХОД: строка (ручной ввод пользователем)
ВЫХОД: строка вида:
"The string contains 2 vowels" - если гласные присутствуют,
"The string doesn't contain vowels" - в противном случае.
Пример:
python ivowels.py - запуск
Вывод:
"Please, enter your string: "
"wHAt Do yOU wANt fRom ME?"
"The string contains 7 vowels"
"Continue? (yes/no) "
"maybe"
"Please, enter corrent answer. Continue? (yes/no) "
"yes"
"Hurray!"
"Please, enter your string: "
"HHHMMMMM..."
"The string doesn't contain vowels"
"Continue? (yes/no) "
"no"
"It was nice to count your vowels!"
"""

VOWELS = "уеіїаоєяию"
will_continue = 'да'

while(will_continue == 'да'):
    line = input("Наберіть текстовий рядок: ").lower()
    num_vowels = 0
    for vowel in VOWELS:
        for symb in line:
            if vowel == symb:
                num_vowels += 1
    print("Рядок містить", num_vowels, "голосних")
    will_continue = input("Будемо продовжувати?(да/ні): ")
                        
