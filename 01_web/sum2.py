"""Написать функционал без использования каких-либо условных выражений,
а применив встроенные функции min() и max(),
который принимает три аргумента - числа X, Y, Z
и возвращает один из вариантов в порядке возрастания значимости:
- X, если Y < X;
- Z, если Y > Z;
- Y, при ином раскладе.

Example of run program:
python xyz.py 3 2 1
>>1
"""

import sys

# if __name__ == "__main__":
#     X = int(sys.argv[1])
#     Y = int(sys.argv[2])
#     Z = int(sys.argv[3])
#     W = int(sys.argv[4])
#     Q = int(sys.argv[5])
#     V = int(sys.argv[6])
#     O = int(sys.argv[7])
# print("POP IT: ", X, " + ", Y, " + ", Z, " + ", W,\
#  " + ", Q, " + ", V , " + ", O, " = ", X+Y+Z+W+Q+V+O)

num = len(sys.argv)
sum = 0
i = 0
print("POP IT: ", end='')
for elem in sys.argv:
    if i == 0:
        i += 1
        continue
    a = int(elem)
    sum += a
    if i!=1:
        print(" + ", end='')
    print(elem, end='')
    i +=1
print(" = ", sum)

