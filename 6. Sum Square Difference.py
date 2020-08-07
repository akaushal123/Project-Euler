def sum_square_natural_number(n):
    return (n * (n + 1) * (2 * n + 1))/6


def sum_natural_number(n):
    return n * (n + 1)/2


def sum_difference(l):
    sum_squares = sum_square_natural_number(l)
    sum_term = sum_natural_number(l)
    return (sum_term * sum_term) - sum_squares


def sum_difference_simplified(n):
    """
        used simplified formula for solving
        Solved formula for
        S1 = 1+2+3+...+n = n*(n+1)/2
        S2 = 1*1 + 2*2 + ... + n*n = n* (n + 1) * (2 * n + 1)/6
        S = S1**2 - S2
        S = (n * (n + 1) * (n-1) * (3*n + 2))/12
    """
    return (n * (n + 1) * (n-1) * (3*n + 2))/12


if __name__ == "__main__":
    limit = int(input("Enter the limit"))
    print(sum_difference(limit))
    print(sum_difference_simplified(limit))