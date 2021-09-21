"""
Задание 6: Классификатор. (бонусное)
УСЛОВИЕ:
Фрагмент кода, который принимает словарь со значениями элементов разных типов,
а возвращает словарь вида {имя_типа : количество_элементов_этого_типа}.
Пример:
{'a': 1, 3: [1,5], 'e': 'abc', '6': []} >> {'str': 1, 'list': 2, 'int': 1}
"""

def typer_list(dct):
	lst_val = list(dct.values())
	dict_oftypes = {}
	for elm_lst in lst_val:
		type_nm = type(elm_lst).__name__
		if type_nm in dict_oftypes:
			dict_oftypes[type_nm] = dict_oftypes[type_nm] + 1
		else:
			dict_oftypes[type_nm] = 1
	return dict_oftypes

if __name__ == "__main__":
	dctn={'a': 1, 3: [1,5], 'e': 'abc', '6': []}
	assert typer_list(dctn) == {'str': 1, 'list': 2, 'int': 1}
	print("Ok!")
	


	

