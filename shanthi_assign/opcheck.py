a=(1,2,3)
a[0]=100

#OP:TypeError: 'tuple' object does not support item assignment
# values of tuples cannot be updated because it is immutable object,once assigned cannot be changed

a=[1,2,3]
a[0]=100
#OP:Out[130]: [100, 2, 3]
#value in index '0' is updated as'100',lists can be updated,deleted 

a="hi"
a[0]=100
#TypeError: 'str' object does not support item assignment
#Strings cannot be updated since it is immutable object.
