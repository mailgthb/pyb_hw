"""
Задание: 
Фрагмент кода, который принимает список со значениями элементов разных типов,
а возвращает словарь вида {элемент : количество_этого_элемента}.
Пример:
['a', 3, 'e', '6', 3, 3, 'a'] >> {'a': 2, 'e': 1, '6': 1, 3: 3}
"""

def repeat_dict(lst):
	dict_rep = {}
	for elm in lst:
		
		if elm in dict_rep:
			dict_rep[elm] = dict_rep[elm] + 1
		else:
			dict_rep[elm] = 1
	return dict_rep

if __name__ == "__main__":
	assert repeat_dict(['a', 3, 'e', '6', 3, 3, 'a']) == {'a': 2, 'e': 1, '6': 1, 3: 3}
	print("Ok!")
	
	

