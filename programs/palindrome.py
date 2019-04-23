a= int(input("Enter the number"))
rev=0
b=a
while (b != 0):
	r=b%10
	rev=rev*10+r
	b=b//10
if (rev == a):
	print("The given number is palindrome")
else:
	print("The given number is not palindrome")	

