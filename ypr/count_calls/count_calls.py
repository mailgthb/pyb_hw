import repeat_dict
import input_tel
import ks_tel


lst_tel = (442362910, 442362910, 442577227, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023,\
	443334023, 443334023, 443334023, 443334023, 443334023, \
	443544131, 443923277, 443923277, 445191919, 462601376)

def compare_kstel_binotel():
	lst_input_tel = input_tel.line.split('\n')
	rep_dict = repeat_dict.repeat_dict(lst_input_tel)

	lst_ks_tel = ks_tel.line.split('\n')

	dict_ks_tel_rep = {}
	for elm in lst_ks_tel:
		dict_ks_tel_rep[elm] = rep_dict.get(elm, 0)
	return dict_ks_tel_rep

dict = compare_kstel_binotel()
for tel, rep in dict.items():
	print(tel, rep)


	
	
	
	
