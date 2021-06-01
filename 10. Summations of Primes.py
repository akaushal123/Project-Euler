"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
"""

def summations_of_primes(limit):
    sum = 0

    prime = [True for _ in range(limit + 1)]

    p = 2

    while p * p <= limit:
        if prime[p]:
            for j in range(p * p, limit + 1, p):
                prime[j] = False
        p += 1

    for p in range(2, limit + 1):
        if prime[p]:
            sum += p

    return sum


if __name__ == "__main__":
    limit = int(input("Enter limit of primes: "))
    print(summations_of_primes(limit))