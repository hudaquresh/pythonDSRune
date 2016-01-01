'Implement the bubble sort' 

def bubblesort(aList): 
	for i in range(0,len(aList)): 
		for pos in xrange(0,len(aList)-1): 
			if aList[pos] > aList[pos+1]: 
				temp = aList[pos]
				aList[pos] = aList[pos+1]
				aList[pos+1] = temp
	return aList

def shortBubbleSort(aList): 
	exchanges = True 
	passnums = len(aList) - 1 
	while passnums > 0 and exchanges: 
		exchanges = False
		for pos in range(0, len(aList) - 1): 
			if aList[pos] > aList[pos + 1]:  
				exchanges = True 
				temp = aList[pos]
				aList[pos] = aList[pos+1]
				aList[pos+1] = aList[pos] 
 		passnums -= 1 
	return aList 
def main(): 
	aList = [3, 4, 1, 5, 2, 3] 
	print bubblesort(aList)
	print shortBubbleSort(aList) 

main() 
