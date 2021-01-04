str1 = input("Enter a non empty string: ")
print("Your string is: ",str1)
if len(str1) == 0:
	print("This is an empty string")
else:
	n = int(input("Enter the value of n in which the character to be removed: "))
	if n<len(str1):
		print("String after removing ",n,"th index character is : \n",str1[0:n]+str1[n+1:str1[-1]])
	else:
		print("Invalid index")
		#use slicing correct the code