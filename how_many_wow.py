"""
Zadanie 3: Podschet vhozhdenij podstroki.

USLOVIE:
Realizovat' podschety kolichestva vhozhdenij podstroki "wow" v stroke.
VHOD: stroka
VYHOD: chislo vhozhdenij podstroki "wow"
Primer:
s = "wowhatamanwowowpalehche"
...
> 3
"""

num_wow = 0
line = input("Наберіть текстовий рядок: ").lower()
for num, symb in enumerate(line):
    if line[num:num+3] == "wow":
    	num_wow += 1
print(num_wow)

