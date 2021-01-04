ls = input("Enter the 2 words separated by a space: ").split(" ")
print("Before swapping ",ls)
str1 = ls[0]
str2 = ls[1]
k = str1[0]
print("After swapping ",str1.replace(str2[0],str1[0],1),str2.replace(str1[0],k,1))