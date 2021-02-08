d1 = {}
d2 = {}
print("Dictionary1::")
n1 = int(input("How many elements? "))
for i in range(n1):
	d1[i] = int(input("Enter value: "))
print("Dictionary2::")
n2 = int(input("How many elements? "))
for i in range(n2):
	d2[i] = int(input("Enter value: "))
print("Dictionary1::",d1)
print("Dictionary2::",d2)
if (n1<n2):
	extra = {i:d2[i] for i in d2 if i>=n1}
	d1.update(extra)
for i in range(0,min(n1,n2)):
	d1[i]=d1[i]+d2[i]
print("Merged dictionary:: ",d1)