def palin(n):
	if n == n[::-1]:
		print("palindrome")
	else:
		print("not a palindrome")
	return

n = raw_input("Enter a String:")

palin(n)

