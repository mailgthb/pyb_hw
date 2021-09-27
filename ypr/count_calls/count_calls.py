import repeat_dict
import input_tel
import ks_tel
import asking_for_info



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

def compare_kstel_binotel_with_rep():
	lst_input_tel = input_tel.line.split('\n')
	rep_dict = repeat_dict.repeat_dict(lst_input_tel)

	lst_ks_tel = ks_tel.line.split('\n')
	lst_ks_tel_rep = []
	for i, elm in enumerate(lst_ks_tel):
		#for elm2 in rep_dict:
		lst_ks_tel_rep.append(rep_dict.get(elm, 0))
	return lst_ks_tel_rep

# def rep_asking_for_info():
# 	lst_asking_for_info = asking_for_info.line.split('\n')
# 	#print(lst_asking_for_info)
# 	num_asking4info_dict = repeat_dict.repeat_dict(lst_asking_for_info)

def compare_kstel_vs_asking_for_info():
	lst_asking_for_info = asking_for_info.line.split('\n')
	#print(lst_asking_for_info)
	num_asking4info_dict = repeat_dict.repeat_dict(lst_asking_for_info)
	lst_ks_tel = ks_tel.line.split('\n')
	lst_ks_tel_rep_ask = []
	for i, elm in enumerate(lst_ks_tel):
		#for elm2 in rep_dict:
		lst_ks_tel_rep_ask.append(num_asking4info_dict.get(elm, 0))
	return lst_ks_tel_rep_ask

	


#Закоментировал, но это работает и нужно, просто сейчас 
#другие функции запускаю.
#dict = compare_kstel_binotel()
# for tel, rep in dict.items():
# 	print(tel, rep)

#Закоментировал, но это работает и нужно, просто сейчас 
#другие функции запускаю.
# lst = compare_kstel_binotel_with_rep()
# for i, rep in enumerate(lst):
#  	print(rep)

	
lst = compare_kstel_vs_asking_for_info()
#print(dict)
for i, num_ask_info in enumerate(lst):
	print(num_ask_info)

	
