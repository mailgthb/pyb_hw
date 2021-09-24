def get_discr(a, b, c):
	d = b ** 2 + 4 * a * c
	return d

def get_eq_root(a, b, d, order=1):
	if order==1:
		x = (-b + d ** (1/2.0)) / (2*a)
	else:
		x = (-b - d ** (1/2.0)) / (2*a)
	return x

def input_parameter(parameter_name='a'):
	while True:
		a = input("Enter the parameter of the equation: %s = " 
			 % parameter_name)
		if a.replace('.', '').isdigit() and float(a) != 0:
			return float(a)			
		else:
			print ("Please enter the number of nonzero!")

def main():
	print("a*x^2 + b*x + c = 0")
	print("Enter the coefficient for the quadratic equation")
	a = input_parameter()
	b = input_parameter('b')
	c = input_parameter('c')
	d = get_discr(a, b, c)
	if d<0:
		print("Rootis doesn't exist")
	else:
		x1 = get_eq_root(a, b, d)
		x2 = get_eq_root(a, b, d, order=2)
		if x1==x2:
			print("There is one root %g" % x1)
		else:
			print("There are roots x1 = %g, x2 = %g" % (x1, x2))

main()