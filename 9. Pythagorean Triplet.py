"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math


def sum_terms(sum):
    for a in range(1, sum + 1):
        for b in range(a, sum + 1):
            c = sum - a - b
            d = math.sqrt(a**2 + b**2)
            if d == c and a < b:
                return {"a": a, "b": b, "c": c}, a * b * c

    return "NO TRIPLET EXISTS FOR GIVEN SUM"


if __name__ == "__main__":
    sum = int(input("Enter sum of terms: "))
    print(sum_terms(sum))