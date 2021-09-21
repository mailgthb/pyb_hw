"""
Задание 3: Триделение.
УСЛОВИЕ:
Фрагмент кода, который принимает список любых чисел и возвращает словарь вида:
{число: boolean}, где: boolean - True или False в зависимости делится ли число на 3
без остатка.
Пример:
[3,7,12] >> {3:True, 12:True, 7:False}
"""

def div_three(thelist):
	listbool = []
	for i in thelist:
		if i%3==0:
			listbool.append(True)
		else:
			listbool.append(False)
	list_of_tuple = zip(thelist, listbool)
	return dict(list_of_tuple)



if __name__ == "__main__":
	assert div_three([3,12,7]) == {3:True, 12:True, 7:False}
	print("Ok!")