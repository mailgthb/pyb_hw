L = ["a", 5, 2, 5, (1, "a"), "a"]

result = []
for item in L:
	if item not in result:
		result.append(item)
print(result)