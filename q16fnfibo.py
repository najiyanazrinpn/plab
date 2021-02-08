def fibo(n):
    f1 = -1
    f2 = 1
    for i in range(n):
    	f3=f1+f2
    	f1,f2=f2,f3
    	print(f3,end=" ")
n = int(input("Enter no: of terms: "))
print("Fibonacci series:",end=" ")
fibo(n)