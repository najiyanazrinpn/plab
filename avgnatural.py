n = int(input("Enter value of n: "))
s = 0
for i in range(1,n+1):
	s+=i
print("Average of first ",n," natural numbers is ",s/n)