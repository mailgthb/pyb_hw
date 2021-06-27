import colorama
from colorama import Fore, Back, Style
colorama.init()

lenDisplay = 85
line = '"...і що сал ?о лас ощ і"'
print()
line_to_print = (Fore.GREEN + "====== А, нумо, створимо дзеркальну анаграму рядка " + Style.RESET_ALL)
line_to_print += F"{line}" + Fore.GREEN + '! =======' + Style.RESET_ALL
print(line_to_print)

# Друк коду першого способу
print('\n')
print( Fore.CYAN + "Перший спосіб".center(lenDisplay, '-') + Fore.RESET )
print( Fore.BLUE + "line[::-1]", end = Fore.CYAN + '  :     ' )
print( Fore.RESET + "   ", end = '' )
# Сам код
print( line[::-1] ) 


# Друк коду другого способу
print('\n')
print(Fore.CYAN + "Другий спосіб".center(lenDisplay, '-'), end = '')
print(Fore.BLUE + """
for elem in reversed(line):
    print(elem, end = '') """, end = Fore.CYAN + ' :     ' )
print( Fore.RESET, end = '')
# Сам код
for elem in reversed(line):
    print(elem, end = '')

    
# Друк коду третього способу
print()      
print()
print(Fore.CYAN + "Третій спосіб".center(lenDisplay, '-'))
print(Fore.BLUE + "text = ''.join(reversed(line) ", end = Fore.CYAN + ' :     ')
print(Style.RESET_ALL, end = '')
# Сам код
text = ''.join(reversed(line))
print(text)


# Друк коду четвертого способу
print()      
print()
print(Fore.CYAN + "Четвертий спосіб".center(lenDisplay, '-'), end = '')
codeText = """
Lline = list(line)
for i in range(len(line) // 2):
    Lline[i], Lline[ -1 - i] = Lline[-1 -i], Lline[i]"""
print(Fore.BLUE + codeText, end = '')                  
print(Fore.CYAN + " : " + Style.RESET_ALL, end = '')
# Сам код
Lline = list(line)
for i in range(len(line) // 2):
    Lline[i], Lline[ -1 - i] = Lline[-1 -i], Lline[i]
print(''.join(Lline))

