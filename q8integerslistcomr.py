n = int(input("Enter number of elements: "))
l1 = [int(input("Enter element ")) for i in range(0,n)]
print("List of positive numbers in ",l1," is ",[i for i in l1 if i>0])