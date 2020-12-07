a = int(input("Enter number1:: "))
b = int(input("Enter number2:: "))
c = int(input("Enter number3:: "))
if a>b and a>c:
	print(a," is largest among ",a,", ",b," and ",c)
elif b>c:
	print(b," is largest among ",a,", ",b," and ",c)
else:
	print(c," is largest among ",a,", ",b," and ",c)