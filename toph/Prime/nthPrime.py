try:
	num = int(input("Find the nth prime (n > 500000 takes too much time)\n--> "))
	#num = 10000
	primeDict = {
		0: 0, 
		10000: 104741, 
		20000: 224741, 
		30000: 350377, 
		40000: 479935, 
		50000: 611953, 
		60000: 746773, 
		70000: 882385, 
		80000: 1020385, 
		90000: 1159529, 
		100000: 1299709,
		110000: 1441049, 
		120000: 1583587, 
		130000: 1726949,
		140000: 1870667,
		150000: 2015177, 
		160000: 2160559, 
		170000: 2307229,
		180000: 2454617, 
		190000: 2601865, 
		200000: 2750159, 
		210000: 2898539, 
		220000: 3047771, 
		230000: 3196937, 
		240000: 3346619, 
		250000: 3497863, 
		260000: 3648937, 
		270000: 3800209, 
		280000: 3951167, 
		290000: 4103639, 
		300000: 4256233,
		310000: 4410319, 
		320000: 4562705, 
		330000: 4716079, 
		340000: 4869875, 
		350000: 5023307, 
		360000: 5178049, 
		370000: 5332529, 
		380000: 5487703, 
		390000: 5644031,
		400000: 5800079,
		410000: 5955041, 
		420000: 6111613, 
		430000: 6268301, 
		440000: 6424957, 
		450000: 6581965, 
		460000: 6738895,
		470000: 6895393, 
		480000: 7052137, 
		490000: 7210777, 
		500000: 7368787
	}

	import math

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

	def nthPrime(n):
		global primeDict
		if n in primeDict:
			return primeDict[n]
		else:
			tempFound = math.floor(n // 10000) * 10000
			if tempFound in primeDict:
				found = tempFound
				if primeDict[found] % 6 == 5:
					temp = primeDict[found] + 2
				else:
					temp = primeDict[found] + 4
			else:
				found = 2
				temp = 5

			if n == 1:
				return 2
			elif n == 2:
				return 3
			else:
				run = True
				while run:
					if found % 10000 == 0:
						if temp % 6 == 5:
							temporary = temp - 4
						else:
							temporary = temp - 2
						primeDict[found] = temporary

					if n == found:
						run = False
					else:
						if isPrime(temp):
							found += 1
							if temp % 6 == 5:
								temp += 2
							else:
								temp += 4
						else:
							if temp % 6 == 5:
								temp += 2
							else:
								temp += 4
			if temp % 6 == 5:
				return temp - 4
			else:
				return temp - 2

	b = True
	print(f"{num}th Prime number is {nthPrime(num)}.")
except:
	print("Input has to be positive integer and nothing else. If you are Sure your input is correct, contact\ntanvirsalehin2988@gmail.com")
	b = False

import turtle
prime = turtle.Turtle()
style = ("Arial", 30, "normal") if b else ("Arial", 20, "normal")
text = f"{num}th Prime number is\n{nthPrime(num)}." if b else ("Input has to be positive integer and nothing else.\nIf you are Sure your input is correct, contact\ntanvirsalehin2988@gmail.com")
prime.write(text, font = style, align = "center")
turtle.exitonclick()
