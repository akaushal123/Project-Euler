"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def sum_dig(x):
    sum = 0
    str_x = str(x)
    for _ in str_x:
        sum += int(_)
    return sum

print(pow(2, 1000))
print(sum_dig(pow(2, 1000)))