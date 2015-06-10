def palin(str):
	if str==str[::-1]:
		print("True:\tThis String is a palimdrome:",str,str[::-1])
	else:
		print("False:\tThis String is not a palindrome:",str,str[::-1])
	return

str=input("Enter a string:")
palin(str)