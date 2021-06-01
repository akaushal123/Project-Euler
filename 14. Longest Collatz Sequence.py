"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

COLLATZ = {1 : 1}

def collatz(n):
    global COLLATZ
    if not n in COLLATZ:
        if n%2 == 0:
            COLLATZ[n] = collatz(n/2) + 1
        else:
            COLLATZ[n] = collatz(3 * n + 1) + 1
    return COLLATZ[n]

for i in range(1000000, 0, -1):
    collatz(i)

max_key = max(COLLATZ, key=COLLATZ.get)
print(max_key, COLLATZ[max_key])



