"""Given an even number (greater than 2), return two prime numbers whose sum will be equal
to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d."""
import commun

def find_prime_sum(num: int):
    # if the number is any number other than four, it can't be 2 and 2
    first = 0
    second = 0

    if num%2 != 0:
        print("INVALID FORMAT MUST BE EVEN")

    def output(num1, num2):
        print(str(num1) + ' + ' + str(num2) + ' = ' + str(num))

    if num == 4:
        return output(2, 2)

    primes = commun.find_prime_upto(num)

    for i in primes:
        if num-i in primes:
            return output(i, num-i)


if __name__ == '__main__':
    find_prime_sum(1024)




