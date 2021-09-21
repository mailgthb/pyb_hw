"""
Задание 2: Симметрия.
УСЛОВИЕ:
Фрагмент кода, который принимает строку и определяет симметрична ли строка.
(Возвращает True или False).
Пример:
"abba" >> True
"arbat" >> False
"""


def symmetry(line):
	return line == line[::-1]

if __name__ == "__main__":
	assert symmetry("abba") == True
	assert symmetry("arbat") == False
	print("Ok!")
	