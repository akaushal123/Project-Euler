"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

"""
 The number of such paths in an m×n grid is (m+nCm)=(m+nCn), where C => Coeff

The reason is quite simple: you must make a total of m+n moves, consisting of m moves down and n to the right, in any order, and there are (m+nm) ways to choose which of the m+n moves are down (or, equivalently, (m+nn) ways to choose which n of them are to the right).
"""

def lattice_path(rows, cols):
    dp =[[0 for _ in range(cols + 1)] for __ in range(rows + 1)]

    for row in range(rows + 1):
        for col in range(cols + 1):
            if row == 0 or col == 0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[row][col]

print(lattice_path(20, 20))
