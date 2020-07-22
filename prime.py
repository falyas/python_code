#
# This approach is okay;
# Another approach would be to use the Sieve of Eratosthenes algm (see p. 118 on CtCi)
# the Sieve of Eratosthenes algm returns a list of primes given a max value
# then, we can check if a number is prime by passing it as the input for this algm
# then, we can check whether the largest number
# returned by the algm is equivelent to it, if so, then it's prime
# another appraoch is to take into consideration tahat the sqrt(N) is sufficient as the highest value to check
# for every number a which divides n evenly, there's a compliment
# b, where a * b = n, if a > sqrt(N), then b < sqrt(N)
# because sqrt(N)^2 = N, so we only need to check a or b
#
def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        #if num is divisible by any i, then it's not prime
        if num%i == 0:
            return False
    return True

# test code
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
