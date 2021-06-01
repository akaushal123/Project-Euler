# -*- coding: utf-8 -*-
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
Created on Fri Dec 28 21:07:57 2018

@author: Abhishek Kaushal
"""

multiple = []

for i in range(3,1000):
    if not i%3 and not i%5:
        multiple.append(i)
    elif not i%3:
        multiple.append(i)
    elif not i%5:
        multiple.append(i)
    else:
        pass

print(multiple)
print(sum((multiple)))
