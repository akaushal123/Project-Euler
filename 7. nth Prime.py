"""
 potential_prime calculates prime number with value 6*n+1 and 6*n-1 (by property that all prime are formed by this way)
 is_prime checks for the prime number formed by the potential_prime
 nth_prime makes a list for the prime numbers of the given limit
"""


def potential_prime(n):
    return [6 * n - 1, 6 * n + 1]


def is_prime(n):
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if (n % i) == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def nth_prime(limit):
    primes = [2, 3]

    if len(primes) == limit:
        return primes

    n = 1
    while len(primes) < limit:
        potential_prime_number = potential_prime(n)
        if is_prime(potential_prime_number[0]):
            primes.append(potential_prime_number[0])
        if is_prime(potential_prime_number[1]):
            primes.append(potential_prime_number[1])
        n += 1

    return primes[limit - 1]


if __name__ == "__main__":
    num = int(input("Enter the term: "))
    print(nth_prime(num))
