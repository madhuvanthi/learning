class foo:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	
	def __str__(self): #__str__ method is a build in function
		return "({0},{1})".format(self.x,self.y)
		

f=foo(2, 3)

print(f.x,f.y)


print(f)



"""str type converter to turn the object to string"""
"""Returns string representation(human readable) of an object"""