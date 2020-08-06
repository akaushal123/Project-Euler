# -*- coding: utf-8 -*-
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
