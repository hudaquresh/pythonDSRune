'''Implemeting a selection sort.
- Improves on bubble sort because uses less swaps.''' 

def selection(aList): 
	# my initial implementation 
	passnum = len(aList)  
	while passnum > 0:
		positionOfMax = 0  
		for pos in range(0,passnum):
			if aList[pos] > aList[positionOfMax]: 
				positionOfMax = pos 
		temp = aList[passnum-1] 
		aList[passnum-1] = aList[positionOfMax] 
		aList[positionOfMax] = temp 
		passnum -= 1
	return aList


def selectionSort(aList): 
	# Selection sort as done by Interactive Python 
	for fillslot in range(len(aList)-1, 0, -1): 
		positionOfMax = 0 
		for location in range(1, fillslot+1): 
			if aList[location] > aList[positionOfMax]: 
				positionOfMax = location
		temp = aList[positionOfMax]
		aList[positionOfMax] = aList[fillslot]
		aList[fillslot] = temp
	return aList 

def main(): 
	aList = [1, 3, 53, 2, 3, 5, 8, 3, 4] 
	print selection(aList) 
	print selectionSort(aList) 
	aList2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print selection(aList2)
	print selectionSort(aList2)  


main() 
