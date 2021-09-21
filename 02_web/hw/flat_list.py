"""
Задание 9: Уплощение строптивого. (бонусное)
УСЛОВИЕ:
Фрагмент кода, который принимает список списков, и делает список "плоским" -
разворачивая элементы внутренних списков во вмещающий список.
Пример:
[[1],[4,8],[6,3,7],[1,3]] >> [1,4,8,6,3,7,1,3]
"""

def flat_list(source_list, res_list=[]):
	for elm in source_list:
		if type(elm).__name__ == 'list':
			flat_list(elm, res_list)
		else:
			res_list.append(elm)
	return res_list



if __name__ == "__main__":
	assert flat_list([[1],[4,8],[6,3,7],[1,3]]) == [1,4,8,6,3,7,1,3]
	print("Ok!")

