import colorama
from colorama import Fore, Back, Style
colorama.init()

START_TITLE_PROGRAM = "====== А, нумо, створимо дзеркальну анаграму рядка "
LEN_DISPLAY = 85

line = '"...і що сал ?о лас ощ і"'
print()
line_to_print = Fore.GREEN + START_TITLE_PROGRAM + Style.RESET_ALL
line_to_print += line + Fore.GREEN + '! =======' + Style.RESET_ALL
print(line_to_print)

# Друк коду першого способу
print('\n')
print(Fore.CYAN + "Перший спосіб".center(LEN_DISPLAY,'-') + Fore.RESET)
print(Fore.BLUE+"line[::-1]", end=Fore.CYAN+'  :     ')
print(Fore.RESET+"   ", end='')
# Сам код
print(line[::-1]) 

# Друк коду другого способу
print('\n')
print(Fore.CYAN+"Другий спосіб".center(LEN_DISPLAY,'-'), end='')
print(Fore.BLUE+"""
for elem in reversed(line):
    print(elem, end='') """, end=Fore.CYAN+' :       ')
print(Fore.RESET, end='')
# Сам код
for elem in reversed(line):
    print(elem, end = '')
    
# Друк коду третього способу
print()      
print()
print(Fore.CYAN + "Третій спосіб".center(LEN_DISPLAY,'-'))
print(Fore.BLUE+"text = ''.join(reversed(line) ", end=Fore.CYAN+' : ')
print(Style.RESET_ALL, end='')
# Сам код
text = ''.join(reversed(line))
print(text)

# Друк коду четвертого способу
print()      
print()
print(Fore.CYAN+"Четвертий спосіб".center(LEN_DISPLAY,'-'), end='')
codeText = """
Lline = list(line)
for i in range(len(line)//2):
    Lline[i], Lline[-1-i] = Lline[-1-i], Lline[i]"""
print(Fore.BLUE+codeText, end='')                  
print(Fore.CYAN + " : " + Style.RESET_ALL, end='')
# Сам код
Lline = list(line)
for i in range(len(line)//2):
    Lline[i], Lline[-1-i] = Lline[-1-i], Lline[i]
print(''.join(Lline))

# Друк коду п'ятого способу
print()      
print()
print(Fore.CYAN + "П'ятий спосіб".center(LEN_DISPLAY,'-'))
# print(Fore.BLUE+"text = ''.join(reversed(line) ", end=Fore.CYAN+' : ')
print(Style.RESET_ALL, end='')
# Сам код
L = list(line)
L.reverse()
text = ''.join(L)
print(text)

# Друк коду шостого способу
print()      
print()
print(Fore.CYAN+"Шостий спосіб".center(LEN_DISPLAY,'-'), end='')
codeText = """
"""
print(Fore.BLUE+codeText, end='')                  
result = []   
for i in line:
    result.insert(0, i)
print(''.join(result))

a, b = 3, 5
print(a, b)