l1 = input("Enter the list of integers: ").split(" ")
l1 = list(map(int,l1))
print("List of positive numbers in ",l1," is ",[i for i in l1 if i>0])
