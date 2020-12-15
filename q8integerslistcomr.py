n = int(input("Enter number of elements: "))
l1 = [int(input("Enter element ")) for i in range(0,n)]
l2 = [i for i in l1 if i>0]
print("List of positive numbers in ",l1," is ",l2)