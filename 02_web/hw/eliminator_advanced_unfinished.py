"""
Задание 7: Сепаратор.Адвансед (бонусное)
УСЛОВИЕ:
Выполнить задание 5 ("Сепаратор") с дополнительным условием:
чтобы входящий список и список возвращаемый были одним и тем же объектом, т.е.
должна произойти модификация списка, а не пересборка нового.
start_list = [1,4,8,6,3,7,1]
end_list = [1,1,3,7,8,6,4]
(start_list is end_list) == True
Пример:
[1,4,8,6,3,7,1] is [1,1,3,7,8,6,4]
"""

def eliminator_advanced(data):
	data.sort()
	find_first_even=-1
	for n, i in enumerate(data):
		if i%2==0:
			find_first_even = n
			break
	data[find_first_even:].sort(reverse = True)
	return data

def eliminator_advanced(data):
	data.sort()
	find_first_even=-1
	preodd = 0
	for n, i in enumerate(data):
		if i%2!=0:
			if i < preodd:
				data[n-1], data[n] = data[n], data[n-1]
				preodd = data[n]
		else:
			flag = swap(data, n)
			if flag == "then even":

			
	data[find_first_even:].sort(reverse = True)
	return data

def sort_num(data3, p):
	for t, i in enumerate(data3):
		

	if i < preodd:
				data[n-1], data[n] = data[n], data[n-1]
				preodd = data[n]

def swap_until_odd(data2, k, m=k):
	if data2[m+1]%2!=0:
		data2[k], data2[m+1] = data2[m+1], data2[k]
		return "end"
	if m+1 == len(data2):
		return "then even"		
	if data2[k+1]%2==0:
		swap_until_odd(data2, k, m+1)

	# even = [i for i in data if i%2==0]
	# even.sort(reverse = True)
	# odd = [i for i in data if i%2!=0]
	# odd.sort()
	# return odd + even

if __name__ == "__main__":
	assert eliminator_advanced([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
	print("Ok!")