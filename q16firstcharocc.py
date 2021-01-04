str1 = input("Enter a non empty string: ")
a = str1[0]
str1 = str1.replace(a,'$')
str1[0] = a
print(str1)