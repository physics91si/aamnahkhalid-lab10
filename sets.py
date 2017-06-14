"""
● Constructor (you should not require any constructor arguments)
● Contains (checks if an element is in the set)
● Add (adds an element to the set)
● Remove (removes an element from the set—should handle case where the element is not in the set)
● Size (returns number of elements in the set)
● Union (see above description—overload the | operator)
● Intersection (see above description—overload the & operator)
● Subtract (see above description—overload the - operator) """

import sys

class Set:	
	def __init__ (self):
		self.List = []
	def contains (self, elem):
		if elem in self.List:
			return True
		else: 
			return False
	def add (self, elem):
		if not self.contains(elem):
			self.List.append(elem)
	def remove(self, elem):
		if self.contains(elem):
			self.List.remove(elem)
		else:
			print("This element is not in the set.\nYou can't lose what you don't have.")
	def size(self):
		return len(self.List)

	def __or__(self, other):
		result = Set()
		for y in self.List:
			result.add(y)
		for x in other.List:
			if not self.contains(x):
				result.add(x)

		return result

	def __and__(self, other):
		result = Set()
		for x in other.List:
			if self.contains(x):
				result.add(x)

		return result
		###except:print("Something crazy is going on. Ae you sure the two are valid sets?"
	def __sub__(self, other):
		result = Set()
		for x in self.List:
			if not other.contains(x):
				result.add(x)

		return result

	def __str__(self):
		return str(self.List)
		"""except:
									print("Something crazy is going on. Ae you sure the two are valid sets?")
						
						"""







