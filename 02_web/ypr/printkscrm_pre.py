import pyperclip

import ourcrm
import ks
import compare


def printkscrm10(lst):
	gap = ' '
	print("          1", gap*10, '2', gap*10, '3', gap*10, '4', \
		gap*10, '5', gap*10, '6', gap*10, '7', gap*10, '8', gap*10, '9', gap*9, '+10')
	print("00  ", end='')
	for i, elm in enumerate(lst):
		if (i+1)%10!=0:
			print(elm, end=' ')
		else:
			print(elm)
			print(i+1," ", end='')

		

f = open('text.txt', 'w')
kievstar = ks.lineks.split('\n')
ourcrm = ourcrm.lineourcrm.split('\n')
Isntin_crm = compare.compare(kievstar, ourcrm)
printkscrm10(Isntin_crm)
len_Isntin_crm = len(Isntin_crm)
pre = ''
print(); print()
for i, elm in enumerate(Isntin_crm):
	print(F"{i+1} з {len_Isntin_crm} ", end='')
	f = open('text.txt', 'w')
	f.write(elm)
	pyperclip.copy(elm)
	pre = elm
	akey = input()
	
f.close()
