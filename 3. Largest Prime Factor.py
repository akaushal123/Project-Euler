import math


def largest_prime_factor(num):
    max_prime = -1

    while num%2 == 0:
        max_prime = 2
        num >>= 1

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            max_prime = i
            num = num/i

    return max_prime


if __name__ == "__main__":
    print(largest_prime_factor(600851475143))