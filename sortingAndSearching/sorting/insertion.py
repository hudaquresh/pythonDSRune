'''Implementing an insertion sort algorithm.'''

def insertionSort(aList): 
	# insertion sort
	for index in range(1, len(aList)): 
		currentValue = aList[index]
		position = index
		while position > 0 and aList[position-1] > currentValue: 
			aList[position] = aList[position-1] 
			position = position-1
		aList[position] = currentValue

	return aList
	
	
def main(): 
	aList = [4, 5, 1, 2, 6, 3, 4, 2, 4, 2, 8, 7, 6, 5] 
	print insertionSort(aList)  
main()

