def diction(n):
	squares = {(x,x*x) for x in range(1,n+1)}
	return squares

n=int(input("Enter a number:"))
i=diction(n)
print(i)