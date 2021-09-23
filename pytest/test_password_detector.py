def decor(func):
	def wrap():
		print("======")
		print(func())
		print("======")
	return wrap

#   Just breaking the string into 3 parts --> Integer, Special Character, Letter
def destructure(string):
	special = ["@", "!", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", '"', "'", "?", "<", "/", ">", "|", "+", "=", "-", "_", "`", "~", ";", ":", ",", "."]
	numCount = 0
	specialCount = 0
	charCount = 0
	for char in string:
		try:
			if int(char) != char:
				numCount += 1
		except ValueError:
			pass
			if char in special:
				specialCount += 1
			else:
				charCount += 1

	return numCount, specialCount, charCount

#   Well, this checks if the password is strong or week
def checkPass(string):
	num, special, char = destructure(string)
	total = num + special + char
	conditions = [num >= 2, special >= 2, char >= 3, total >= 7]
	if all(conditions):
		return "Storng"
	else:
		return "Weak"

#   Use pytest to test this...
def test():
	tests = [
		{
			"name": "Test 1",
			"input": "665{[;hycw61i0",
			"expected": True
		},
		{
			"name": "Test 2",
			"input": "",
			"expected": False
		},
		{
			"name": "Test 3",
			"input": "yqufuyv3iubc[[]00ncwb1",
			"expected": True
		},
		{
			"name": "Test 4",
			"input": "weferver",
			"expected": False
		},
		{
			"name": "Test 5",
			"input": "[[][3][]]",
			"expected": False
		},
		{
			"name": "Test 6",
			"input": "aa22::",
			"expected": False
		}
	]

	for test in tests:
		assert test["expected"] == checkPass(test["input"]), test["name"]

@decor
def run():
	print(checkPass("vwefcyv"))
run()
