def compare(kievstar, ourcrm):
	isnoin_crm=[]
	for thetel_ks in kievstar:
		for thetel_crm in ourcrm:
			if thetel_ks == thetel_crm:
				break
		else:
			isnoin_crm.append(thetel_ks)
	return isnoin_crm


if __name__ == "__main__":
	assert compare(['a', 'e', 'a', 'g'], ['a', 'b', 'd']) == ['e', 'g']
	print("Ok!")