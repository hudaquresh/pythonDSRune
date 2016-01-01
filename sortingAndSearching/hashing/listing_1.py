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


def hashModified(aString, tableSize): 
	# A modified version of the hash function to account for anagrams
	
	sum = 0 
	for pos in range(len(aString)):
		sum = sum + ord(aString[pos])*(pos + 1)
	return sum%tableSize 

if __name__ == '__main__': 
	
	#TODO  Practice writing test cases 
	#TODO  Test more interesting examples  
	var1 = hash('cat', 11)
	print var1
	assert var1 == 4 

	var2 = hashModified('cat', 11)
	print var2
	assert var2 == 3

