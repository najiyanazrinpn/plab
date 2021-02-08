def fact(n):
	f = 1
	for i in range(1,n+1):
		f*=i;
	return(f)
n = int(input("-----FACTORIAL-----\nEnter the value of n: "))
print(n,"! = ",fact(n))