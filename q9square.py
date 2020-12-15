n = int(input("Enter the value of n: "))
s = 0
for j in [i**2 for i in range(1,n+1)]:
	s+=j
print(s)