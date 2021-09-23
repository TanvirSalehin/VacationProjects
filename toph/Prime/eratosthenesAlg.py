import math

def primesLessThan(n: int) -> list[int]:
	if n <= 2:
		return []
	is_prime = [True] * n
	is_prime[0] = False
	is_prime[1] = False

	for i in range(2, math.isqrt(n)):
		if is_prime[i]:
			for x in range(i**2, n, i):
				is_prime[x] = False

	return prime


print(primesLessThan(10000))
