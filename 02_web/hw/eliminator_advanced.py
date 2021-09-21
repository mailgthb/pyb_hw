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

def eliminator_advanced(a):
	lenlist = len(a)
	for j in range(lenlist):
		for i in range(lenlist-1):
			if a[i]%2!=0 and a[i+1]%2!=0:
				if a[i]>a[i+1]:
					a[i], a[i+1] = a[i+1], a[i]
			elif a[i]%2==0:
				if a[i+1]%2!=0:
					a[i], a[i+1] = a[i+1], a[i]
				elif a[i+1]%2==0:
					if a[i+1] > a[i]:
						a[i], a[i+1] = a[i+1], a[i]
	return a

if __name__ == "__main__":
	assert eliminator_advanced([1,4,8,6,3,7,1]) == [1,1,3,7,8,6,4]
	print("Ok!")