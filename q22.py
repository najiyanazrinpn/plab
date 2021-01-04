list1 = input("Enter integer list1: ").split(' ')
list2 = input("Enter integer list2: ").split(' ')
list1 = list(map(int,list1))
list2 = list(map(int,list2))
if len(list1) == len(list2):
    print("Lists are of same length")
else:
    print("Lists are of different length")
if sum(list1) == sum(list2):
    print("Sum of list1 = Sum of list2")
else:
    print("Sum of list1 not equal to sum of list2")
inter = []
for i in list1:
	for j in list2:
		if i==j and i not in inter:
			inter.append(i)
if inter:
    print("Common elements: ",inter)
else:
    print("No common elements")