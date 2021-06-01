"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math


def smallest_multiple(upper_limit_val):
    # it's the LCM from 1 to upper_limit
    answer = 1
    for i in range(1, upper_limit_val + 1):
        answer = int(answer * i / math.gcd(answer, i))

    return answer


if __name__ == "__main__":
    upper_limit = int(input("Enter Range: "))
    print(smallest_multiple(upper_limit))
