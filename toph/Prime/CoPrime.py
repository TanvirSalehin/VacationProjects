n = int(input("Write the number\n--> "))
import math
#n = 10000000

def isPrime(num):
	snum = math.floor(math.sqrt(num))
	if num == 2:
		return True
	elif num % 2 == 0:
		return False
	else:
		for i in range(3, snum + 1, 2):
			if num % i == 0:
				return False
	return True

def coPrime(n):
	if isPrime(n):
		return {0}
	setn = set()
	run1 = True
	temp1 = 2
	while run1:
		if temp1 < n:
			if  n % temp1 == 0:
				run = False
				if (n / temp1) - temp1 >= 0:
					setn.add(temp1)
					setn.add(int(n / temp1))
				else:
					run = False
				temp1 += 1
			else:
				temp1 += 1
		else:
			run1 = False
	li = []
	for i in setn:
		if not isPrime(i):
			li.append(i)
	for j in li:
		setn.remove(j)

	return setn

if not (r := coPrime(n)) == {0}: 
	p = n
	for i in r:
		p = p * (1 - 1 / i)
	textNum = int(p)
	print("There are ", int(p), " numbers co-prime to", n)
else:
	textNum = n - 1
	print("There are ", n - 1, " numbers co-prime to", n)

import turtle
coprime = turtle.Turtle()
style = ("Arial", 30, "normal")
text = f"There are \n{textNum}\nnumbers co-prime to \n{n}"
coprime.write(text, font = style, align = "center")
turtle.exitonclick()
