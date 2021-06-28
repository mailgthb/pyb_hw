import colorama
from colorama import Fore, Back, Style
colorama.init()

line = input("Наберіть текстовий рядок: ").lower()
num_wow = line.count("wow")
print(num_wow)

