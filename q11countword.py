text = input("Enter the line of text: ").split(" ")
list1 = []
for i in text:
	if i not in list1:
		list1.append(i)
text = " ".join(text)
for i in list1:
	print("No: of occurences of ", i, " :: ", text.count(i))
	