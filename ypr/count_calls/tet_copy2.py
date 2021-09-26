lst_tel0 = (442362910, 442362910, 442577227, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023, \
	443544131, 443923277, 443923277, 445191919, 462601376)

dct_num_rep = {}
n=0
while n<len(lst_tel0):
	elm = lst_tel0[n]
	dct_num_rep[elm] = 1
	print(dct_num_rep)
	k = n + 1
	while k<len(lst_tel0):
		if elm == lst_tel0[k]:
			dct_num_rep[elm] += 1
		else:
			n=k
			break
		k += 1
	n += 1


	
	
	
	
