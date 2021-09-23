def Hi(*args):
	sum = 0
	for i in args:
		sum += i
	return sum

print(Hi(1, 4, 3, 54, 63, 87))

