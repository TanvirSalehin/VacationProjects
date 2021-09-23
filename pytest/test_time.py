import timeit
#num = int(input())
hello = 10000

num = 10000
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
	if 0 < n <= 500000:
		if n == 1:
			return 2
		else:
			run = True
			temp = 2
			found = 0
			while run:
				if n == found:
					run = False
				else:
					if isPrime(temp):
						found += 1
						temp += 1
					else:
						temp += 1
	else:
		return 'Stop It'
	return temp - 1

#nthPrime(num)
#print(isPrime(9))

import timeit
print(max(timeit.repeat(
		setup = "import math",
		stmt = isPrime(num),
		number = 1,
		repeat = 10
	)))
