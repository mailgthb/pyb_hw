def compare_set_common(kievstar, ourcrm):
	kievstar_set = frozenset(kievstar)
	ourcrm_set = frozenset(ourcrm)
	common_set = kievstar_set & ourcrm_set
	return common_set



if __name__ == "__main__":
	for elm in compare_set_common(['a', 'e', 'a', 'g', 'v'], ['a', 'v', 'b', 'd']):
		print(elm)
	assert compare_set_common(['a', 'e', 'a', 'g', 'v'], ['a', 'v', 'b', 'd']) == {'a', 'v'}
	print("Ok!")