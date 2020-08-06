# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:13:26 2018

@author: Abhishek Kaushal
"""

"""
Fib:- 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
Even Term Fib:- 0, 2, 8, 34, 144
                c = a + 4*b
"""


def sum_even(limit):
    a = 0
    b = 2
    t = 2
    sum = 0
    while t <= limit:
        sum += t
        t = 4*b + a
        a = b
        b = t

    return sum


print(sum_even(4e6))
