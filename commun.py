""" all the basic functions that are used over and over again """

def find_prime_upto(n):
    def isPrime(num):
        for i in range(2, num-1):
            if num%i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)

    return primes

