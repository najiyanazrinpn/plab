n = int(input("How many elements? "))
d = {}
key=''
for i in range(0,n):
	value = int(input("Enter value: "))
	d[i] = value
print("Your dictionary is: \n\t",d)
for i in range(0,n-1):
	for j in range(i,n):
		if(d[i]<d[j]):
			d[i],d[j]=d[j],d[i]
print("Sorted dictionary in ascending order: \n\t",d)
for i in range(0,n-1):
	for j in range(i,n):
		if(d[i]>d[j]):
			d[i],d[j]=d[j],d[i]
print("Sorted dictionary in descending order: \n\t",d)
