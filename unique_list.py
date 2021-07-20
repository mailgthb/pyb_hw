"""принимает список елементов и убирает из него все дубликаты
(формирует список уникальных элементов)."""

the_list = []

the_list = ["a", 5, 2, 5, (1, "a"), "a"]

i = 0
while i < len(the_list):
    j = i + 1
    while j < len(the_list):
        if the_list[i] == the_list[j]:
            the_list.pop(j)
        else:
            j += 1
    i += 1

print(the_list) 
