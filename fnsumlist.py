def sumlist(n):
	sum = 0
	for i in n:
		sum+=i
	return sum
n = (input("Enter the list of numbers: ")).split(" ")
n = list(map(int,n))
print("Sum of integers in the list",sumlist(n))