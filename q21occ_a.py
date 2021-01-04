lst = input("Enter a list: ").split(' ')
c = 0
for element in lst:
    c+=element.count('a')
for element in lst:
    c+=element.count('A')
print("No: of occurence of a in the given list is",c)