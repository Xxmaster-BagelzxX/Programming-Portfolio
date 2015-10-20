# Python learning exercises

# functions
def echo(thing):
	return thing

def swap(n1, n2):
	return n2, n1

	
def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing swap('one, two'): ", swap('one', 'two')
	

#Arithmetic Functions
def reverse(x):
	return -x

def plus(x, y):
	return x + y

def diff(x, y):
	return x - y
	
def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-99): ", reverse(-99)
	print "test plus(4, 3): ", plus(4, 3)
	print "test diff(99, 98): ", diff(99, 98)

def main():
	main_function()
	main_arithmetic()



main()