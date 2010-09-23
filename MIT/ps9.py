# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    	def area(self):
        	raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    	def __init__(self, h):
        	"""
        	h: length of side of the square
        	"""
        	self.side = float(h)
    	def area(self):
        	"""
        	Returns area of the square
        	"""
        	return self.side**2
    	def __str__(self):
        	return 'Square with side ' + str(self.side)
    	def __eq__(self, other):
        	"""
        	Two squares are equal if they have the same dimension.
        	other: object to check for equality
        	"""
        	return type(other) == Square and self.side == other.side

class Circle(Shape):
    	def __init__(self, radius):
        	"""
        	radius: radius of the circle
        	"""
        	self.radius = float(radius)
    	def area(self):
        	"""
        	Returns approximate area of the circle
        	"""
        	return 3.14159*(self.radius**2)
    	def __str__(self):
        	return 'Circle with radius ' + str(self.radius)
    	def __eq__(self, other):
        	"""
        	Two circles are equal if they have the same radius.
        	other: object to check for equality
        	"""
        	return type(other) == Circle and self.radius == other.radius
#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.


class Triangle(Shape):
	def __init__(self,base,height):
		
		self.bs = float(base)
		self.ht = float(height)
	def area(self):
		return (1/2.0)*self.bs*self.ht
	def __str__(self):
		return 'Triangle with base '+ str(self.bs)+'and height '+str(self.ht)
	def __eq__(self,other):
		return isinstance(other,Triangle) and other.bs == self.bs and other.ht == self.ht
#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    	def __init__(self):
        	"""
        	Initialize any needed variables
        	"""
        	## TO DO
		self.k=[]
		self.n=len(self.k)
    	def addShape(self, sh):
        	"""
        	Add shape sh to the set; no two shapes in the set may be
        	identical
        	sh: shape to be added
        	"""
        	## TO DO
		#print sh
		l=obje(sh)
		for i in self.k:
			j=obje(i)
			#print l
			#print j
			if l==j:
				return
		self.k.append(sh)
		#print self.k
		return self.k
				
    	def __iter__(self):
        	"""
        	Return an iterator that allows you to iterate over the set of
        	shapes, one shape at a time
        	"""
        	## TO DO
		return self
	
	def next(self):
		if self.n == 0:
			raise StopIteration
		self.n = self.n-1
		return self.k[self.n]
    	def __str__(self):
        	"""
        	Return the string representation for a set, which consists of
        	the string representation of each shape, categorized by type
        	(circles, then squares, then triangles)
        	"""
		self.k.sort()
		return str(self.k)
        	## TO DO
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    	"""
    	Returns a tuple containing the elements of ShapeSet with the
       	largest area.
    	shapes: ShapeSet
    	"""
    	## TO DO
	j=0
	for i in shapes:
		y=obje(i)
		k=y.area()
		if j==0 or k>j:
			j=k
			w=i
	return (w,j)

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
	"""
    	Retrieves shape information from the given file.
    	Creates and returns a ShapeSet with the shapes found.
    	filename: string
    	"""
    	## TO DO
    	f=open(filename,'r')
	n=ShapeSet()
	x=[]
    	for line in f:
		h=line.split(',')
		x=n.addShape(h)
	#print x
	#for i in n:
		#print i
	d=findLargest(x)
	print "The one with largest area is" + str(d)
	print n

def obje(lis):
	g=Square(3)
	#print lis
	if lis[0]=='square':
		g = Square(lis[1])
	elif lis[0]=='circle':
		g = Circle(lis[1])
	elif lis[0]=='triangle':
		g = Triangle(lis[1],lis[2]) 
	else:
		return 'no comparable objects'
	return g
