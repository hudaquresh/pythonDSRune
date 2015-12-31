"""Computes the factorial of a given number n"""

def factorial(n): 
	'Computes the facotrial recursively' 
	if n <= 1: 
		return 1
	else: 
		return n*factorial(n-1)

def main(): 
	print '2', factorial(2)
	print '3', factorial(3)
	print '4', factorial(4)
	print '5', factorial(5)

if __name__ == '__main__': 
	main() 	 
