import time

def timeit(fn):

	def g(*args, **kwargs):

		start = time.perf_counter()

		x = fn(*args, **kwargs)

		stop = time.perf_counter()

		print("call took", 1e3 * (stop - start), "ms")

		return x

	return g

def is_prime(x):
	for i in range(2, x):
		if x % i == 0:
			return True
	return False

def sum_primes_below(n):

	x = 0
	for i in range(2, n):
		if is_prime(i):
			x += i
	return x

def main():
	s = timeit(sum_primes_below)
	s(1000)

if __name__ == '__main__':
	main()