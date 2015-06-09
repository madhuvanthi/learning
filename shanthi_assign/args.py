
def test(a,*args,**kwargs):
	print()
	print("Values in normal argument:",a)
	#print()
	print("\nvalues in *args:",args)
    
	for i in args:
		print(i)

	print("values in *kwargs:",kwargs)

	for key,value in kwargs.items():
		print(key,value)

  
t=[10,20,"hello"] #lists
test(*t,f=4,g=8)

t=('A','B',3,"five",6,7) #tuples
test(*t,e=1,l=9)

test(a=100,b=200,c=300,d=400,e='hi')

"""*args are used in function definition when we want to pass variable number of arguments(non key-worded) to the function. 
ie..the number of arguments are dynamically changing based on user requirements.

**kwargs are known as key-worded arguments or named arguments.it used to pass the variable number of key-worded arguments based
on the user needs or when the number of arguments needed is unknown.
**kwargs is a dictionary, where everything is in key-value pairs.
The values can be accessed through keys. It maps the values with respective keys, since the values displayed during are unordered"""
