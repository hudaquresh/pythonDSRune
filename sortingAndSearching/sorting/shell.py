'''Implementing a shell sort'''
# TODO My understanding of the shell sort could use some work 
def shellSort(aList): 
	sublistCount = len(aList) // 2
	while sublistCount > 0: 
		for startPosition in range(0, sublistCount): 
			gapInsertionSort(aList, startPosition, sublistCount) 
		print "After increments of size " + str(sublistCount) + "the list is ", aList
	
		sublistCount = sublistCount // 2
	return aList 

def gapInsertionSort(aList, start, gap): 
	for i in range(start + gap, len(aList), gap): 
		currentValue = aList[i]
		position = i
		while position >= gap and aList[position - gap] > currentValue: 
			aList[position] = aList[position - gap] 
			position = position - gap
		aList[position] = currentValue  

def main(): 
	aList = [54, 26, 93, 17, 77, 1, 44, 55, 20] 
	print shellSort(aList)



main() 	
