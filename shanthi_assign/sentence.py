def sen(x):

	words = x.split()
	sentence_rev = " ".join(reversed(words))
	print(sentence_rev)

	#print(words)
	return sentence_rev
s=input("Enter a sentence:")
c=sen(s)
if s==c:
	print("It is a palindrome")
else:
	print("It is not a palindrome")

