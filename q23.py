n = int(input("Enter an integer:"))
val=''
for i in range(1,n+1):
	val=val+"+"+str(n)*i
print(val[1:])