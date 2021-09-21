import pyperclip

import ourcrm
import ks
import compare
import compare_set_common
import printkscrm10
import compare_set_diff
import ks_kont

kievstar = ks.lineks.split('\n')
ourcrm = ourcrm.lineourcrm.split('\n')
kievstar = ks_kont.lineks_kont.split('\n')



def compare_list_one_by_one():
	'''
	код що далі - 
	drukuye po odnomu elementu, одночасно записуючи в буфер обміну, а також у файл.
	Відкрив також другий файл, щоб записувати туди попередній елемент, на всяк 
	випадок, але поки що не зробив цього.

	Drukuye всі результати, тобто "апельсин, яблуко"(ks) і "апельсин, ківі"(crm) 
	видає в результаті "яблуко". 
	'''
	f = open('text.txt', 'w')
	f2 = open('textnext.txt', 'w')
	Isntin_crm = compare.compare(kievstar, ourcrm)
	# это я сравниваю результат двоих операций, на разных алгоритмах построенное:
	# oye = compare_set_diff.compare_set_diff(kievstar, ourcrm)
	# print(oye == set(Isntin_crm))
	printkscrm10.printkscrm10(Isntin_crm)
	len_Isntin_crm = len(Isntin_crm)
	pre = ''
	print(); print()
	for i, elm in enumerate(Isntin_crm):
		print(F"{i+1} з {len_Isntin_crm} ", end='')
		f2 = open('textnext.txt', 'w')
		f2.write(pre)

		f = open('text.txt', 'w')
		f.write(elm)
		pyperclip.copy(elm)
		pre = elm
		akey = input()
	f.close()
	f2.close()

def compare_set_common_one_by_one():
	'''
	код що далі - 
	drukuye po odnomu elementu, одночасно записуючи в буфер обміну, а також у файл.
	Відкрив також другий файл, щоб записувати туди попередній елемент, на всяк 
	випадок, але поки що не зробив цього.

	Drukuye всі результати, тобто "апельсин, яблуко"(ks) і "апельсин, ківі"(crm) 
	видає в результаті "апельсин". 
	'''
	f = open('text.txt', 'w')
	f2 = open('textnext.txt', 'w')
	Isntin_crm = compare_set_common.compare_set_common(kievstar, ourcrm)
	printkscrm10.printkscrm10(Isntin_crm)
	len_Isntin_crm = len(Isntin_crm)
	pre = ''
	print(); print()
	for i, elm in enumerate(Isntin_crm):
		print(F"{i+1} з {len_Isntin_crm} ", end='')
		f2 = open('textnext.txt', 'w')
		f2.write(pre)

		f = open('text.txt', 'w')
		f.write(elm)
		pyperclip.copy(elm)
		pre = elm
		akey = input()
	f.close()
	f2.close()

def admin():
	print("Виберіть що ви хочете зробити:")
	print('1 = апельсин, яблуко"(ks) і "апельсин, ківі"(crm) \
	видає в результаті "яблуко".' )
	print('2 = апельсин, яблуко"(ks) і "апельсин, ківі"(crm) \
	видає в результаті "апельсин".' )
	option = input("Виберіть що ви хочете зробити(наберіть 1 або 2): ")
	if option == '1':
		compare_list_one_by_one()
	elif option == '2':

		compare_set_common_one_by_one()
		

admin()