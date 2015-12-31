'''We write a function called hash that takes a string and a table size and 
returns the hash value in the range from 0 to tablesize - 1.'''

import unittest


def hash(aString, tableSize): 
	# Determines the sum of the ordinals of the string 
	# Returns the remainder of the ordinal value sum divided by tablesize
	
	sum = 0 
	for pos in range(len(aString)): 
		sum += ord(aString[pos]) 
	return sum%tableSize


if __name__ == '__main__': 
	
	# Test a few values 
	Test
