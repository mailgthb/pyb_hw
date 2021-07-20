"""принимает список елементов и убирает из него все дубликаты
(формирует список уникальных элементов)."""

from  more_itertools import unique_everseen

items = ["a", 5, 2, 5, (1, "a"), "a"]
new_list = list(unique_everseen(items))
print(new_list)
