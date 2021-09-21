import sys
print (sys.argv)

import utils

print(utils.a)
utils.p()

if len(sys.argv) < 3:
	print("2 args are needed")
	quit()

if __name__ == "__main__":
	print(sys.argv[1] + ": " + sys.argv[2])
	if sys.argv[1].isdigit() and sys.argv[2].isdigit():
		print(int(sys.argv[1]) + int(sys.argv[2]))