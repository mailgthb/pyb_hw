"""
Задание 1: Квадраты.
УСЛОВИЕ:
Фрагмент кода, который принимает набор (список, кортеж) чисел и возвращает набор
ТОГО ЖЕ типа со значениями квадратов этих чисел.
Пример:
[1,2,3] >> [1,4,9]
(1,2,3) >> (1,4,9)
"""

data = input("Enter data: ")
if data[0] == '[':
	words = data[1:-1].split(',')
	print(words)
	data = [int(i) for i in words]
	print(data)
	quadrate = [i**2 for i in data]

if data[0] == '(':
	words = data[1:-1].split(',')
	data2 = [int(i) for i in words]	
	quadrate = [i**2 for i in data2]
	quadrate = tuple(quadrate)

print(quadrate)
