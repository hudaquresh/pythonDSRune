'''We implement the map abstract data type. This is a useful type commonly used in python known as a dictionary. 

Hash functions/method is an extremeley important concept in computer science. They allow us
to have an efficient lookup in constant time or in other words O(1). Of course the are worst
cases that prevent this good time. 

There are several methods we learned today to produce hash functions. They include the 
remainder method, folding method, and midsquare method. 

We also learned about perfect hash functions and how they typically are hard to find because 
of collisions. We learned about ways to deal with collisions by simply determining a new rehash 
value that will attempt to find an empty slot. 

We want creative solutions to the rehash method because just basic linear probing can lead to clustering.
As a result we use methods that allow for the rehash function to skip over spaces in order to jump to 
a slot a bit farther away to avoid clustering. Also we want to make sure that we go through all slots to 
see if they actually can be used (ie they contain nothing); thus, it is desirable to make the size of the 
hash table a prime number so that any linear probing skip step method will be able to visit all slots. 

Lastly to sum up. What we did was essentially create a dictionary class in python using a hashtable.''' 

class HashTable():
	# Utilize two slots. One for keys and one for data to implement hash table 
	def __init__(self): 
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def hashfunction(self, key, size):  
		#returns the hash value of the key 
		return key%size

	def rehash(self, oldhash, size): 
		# returns a rehash of the old value
		return (oldhash + 1)%size 

	def put(self, key, data): 
		# Mimics the put funciton for a dictionary 
		hashvalue = self.hashfunction(key, len(self.slots))
		if self.slots[hashvalue] == None: 
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			nextSlot = self.rehash(hashvalue, len(self.slots))
			while self.slots[nextSlot] != None and self.slots[nextSlot] != key: 
				nextSlot = self.rehash(nextSlot, len(self.slots)) 
			if self.slots[nextSlot] == None: 
				self.slots[nextSlot] = key
				self.data[nextSlot] = data
			else: 
				self.data[nextSlot] = data # replaces old data with new data
	def get(self, key): 
		# Mimics the get function for a dictionary
		startSlot = self.hashfunction(key, len(self.slots))
		
		data = None
		found = False
		stop = False 
		position = startSlot 
		while self.slots[position] != None and not found and not stop: 
			if self.slots[position] == key: 
				found = True 
				data = self.data[position]
			else: 
				position = self.rehash(position, len(self.slots))
				if position == startSlot: 
					stop = True 
		return data 

	def __getitem__(self, key): 
		return self.get(key)
	
	def __setitem__(self, key, data): 
		self.put(key,data) 

def main():
	H = HashTable()
	H[54] = 'CAT'
	H[22] = 'dog'
	H[23] = 'pup'
	H[34] = 'lion'
	H[45] = 'dolphin'
	H[64] = 'cat' 
	H[72] = 'puppy'  
	print H.slots
	print H.data
	

if __name__ == '__main__': 
	main()  
	
				 
			 
				
	
	
