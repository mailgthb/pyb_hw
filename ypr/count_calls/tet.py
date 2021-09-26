lst_tel0 = (442362910, 442362910, 442577227, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023, \
	443544131, 443923277, 443923277, 445191919, 462601376)

dct_fruit = {}
n=0
while n<len(lst_tel0):
	elm = lst_tel0[n]
	dct_fruit[elm] = 1
	print(dct_fruit)
	for k, item_to_check in enumerate(lst_tel0[n+1:]):
		if elm == item_to_check:
			dct_fruit[elm] += 1
		else:
			n=k+1
			break
	n += 1