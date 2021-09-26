lst_tel = (442362910, 442362910, 442577227, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023, \
	443544131, 443923277, 443923277, 445191919, 462601376)


def count_calls(lst):

	dct_num_rep = {}
	n=0
	while n<len(lst):
		elm = lst[n]
		dct_num_rep[elm] = 1
		print(dct_num_rep)
		
		k = n
		while k<len(lst):
			k += 1
			if elm == lst[k]:
				dct_num_rep[elm] += 1
			else:
				n=k
				break
	return dct_num_rep

def main(lst_tel):
	dct_num_rep = {}
	
	return dct_num_rep

print("fruit:")
print(main(lst_tel))
		


	


	
	
	
	
