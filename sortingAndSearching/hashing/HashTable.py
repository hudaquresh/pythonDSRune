'''We implement the map abstract data type. This is a useful type commonly used in python known as a dictionary. 

Important Topics Covered
- Hashing O(1) for best case
- Hash functions: remainder, folding, and midsquare
- Collisions
	- open addressing
	- linear probing (can lead to clustering) 
	- quadratic probing
	- rehash functions
	- chaining 
'''

# TODO Read more on the analysis of Hashing  
# TODO Write more test cases

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
	
				 
			 
				
	
	
