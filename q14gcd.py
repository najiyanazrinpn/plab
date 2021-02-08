print("-----GCD-----")
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
# for i in range(1,min(n1,n2)+1):
# 	if (n1%i == 0) and (n2%i == 0):
# 		gcd = i
# print()
print("gcd(",n1,",",n2,")=",[i for i in range(1,min(n1,n2)+1) if (n1%i == 0) and (n2%i == 0)][-1],sep="")
