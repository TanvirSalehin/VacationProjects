filename = str(input("Filename:   (with extension .txt)\n-->"))

def common(list1, list2):     #   Intersection of list1 and list2
	list3 = [value for value in list1 if value in list2]
	return list3

def charCount(text, char):     #   Returns how many times a character is on the text
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count

def chars(text):     #   Returns a list of all the characters in the text
	alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	list1 = []
	for c in text:
		if not c in list1:
			list1.append(c)
	list2 = common(alphabets, list1)
	return list2

def charNum(text, list1):     #   returns a list containing how many times a character is in the text corresponding to list from char(text)
	list2 = []
	for c in list1:
		list2.append(charCount(text, c))
	return list2

def percentageShow(list1, list2):     #   Prints the percentage of each character occurance. Return is None
	totalChar = sum(list2)
	for i in range(len(list1)):
		char = list1[i]
		count = list2[i]
		percent = round((count / totalChar) * 100, 3)
		print("{char}  ({count})    :    {percent}%".format(char = char, percent = percent, count = count,))

with open(filename, "r") as file:
	content = file.read()



#     MAIN
#---------------

characters = chars(content)
numList = charNum(content, characters)
percentageShow(characters, numList)
