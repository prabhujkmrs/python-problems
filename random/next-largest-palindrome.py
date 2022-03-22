# You will be given a positive integer N. Your task is to 
# find the smallest number greater than or equal to N that is a prime and a palindrome.


# Example 1:

# Input: N = 12
# Output: 101
# Example 2:

# Input: N = 4
# Output: 5

import math


def prime_palindrome(n: int) -> int:
    while True:
        if n == reverse(n) and isprime(n):
            break
        n += 1

    return n


def isprime(num: int) -> bool:
    if num < 2:
        return False

    is_prime = True
    # Minor optimisation, modify the range to sqrt of the number. 
    # A composite number must have a factor less than or equal to the square root of the number
    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if (num % i) == 0:
            is_prime = False
            break

    return is_prime


def reverse(num: int) -> int:
    snum = str(num)
    rev = snum[::-1]

    return int(rev)


print(prime_palindrome(102))
