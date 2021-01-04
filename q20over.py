lst = input("Enter a list of integers: ").split(" ")
lst = list(map(int,lst))
for i in range(len(lst)):
    if lst[i] > 100:
        lst[i] = 'over'
print(lst)