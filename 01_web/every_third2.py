"""Реализовать функционал который принимает кортеж
и возвращает прореженный кортеж, оставляя только каждый третий элемент.
Реализовать задачу двумя разными вариантами.
Пример:
t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')
> (3,6,9,'b')
Другий варіант: з допомогою циклу"""

t = (1,2,3,4,5,6,7,8,9,0,'a','b','c')

l = []

for elem in t:
    if (t.index(elem)+1)%3 == 0:
        l.append(elem)
        
l = tuple(l)
print(l)
