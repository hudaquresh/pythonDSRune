'''Implement their version of Quicksort'''

def quickSort(aList): 
	quickSortHelper(aList, 0, len(aList) - 1) 

def quickSortHelper(aList, first, last): 
	if first < last: 
		splitpoint = partition(aList, first, last) 
		quickSortHelper(aList, first, splitpoint-1) 
		quickSortHelper(aList, splitpoint+1, last) 


def partition(aList, first, last): 
	pivot = aList[first]
	leftMark = first + 1
	rightMark = last
	
	done = False 
	while not done: 
		while leftMark <= rightMark and aList[leftMark] <= pivot: 
			leftMark += 1 
		while aList[rightMark] >= pivot and rightMark >= leftMark: 
			rightMark -= 1 
		if rightMark < leftMark: 
			done = True 
		else: 
			temp = aList[leftMark] 
			aList[leftMark] = aList[rightMark]
			aList[rightMark] = temp 
	temp = aList[first] 
	aList[first] = aList[last]
	aList[last] = aList[first] 
	
	return rightMark 

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
		
	
