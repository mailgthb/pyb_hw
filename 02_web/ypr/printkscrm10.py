def printkscrm10(lst):
	'''
	Drukuye всі результатиe у вигляді таблиці.Рядки нумерує від 00, 10, 20...
	 Зверху стовпчики нумерує від 1 до 9, а останній стовчик називає "+10".
	 Щоб зрозуміло було, що до числа назви рядка варто додати +10
	'''
	gap = ' '
	print("          1", gap*10, '2', gap*10, '3', gap*10, '4', \
		gap*10, '5', gap*10, '6', gap*10, '7', gap*10, '8', gap*10, '9', gap*9, '+10')
	print("00  ", end='')
	f_all = open('text_all.txt', 'w')
	for i, elm in enumerate(lst):
		if (i+1)%10!=0:
			print(elm, end=' ')
		else:
			print(elm)
			print(i+1," ", end='')
		f_all.write(elm + '\n')
	f_all.close()