"""
Consider an m x n checkerboard. On each cell of the checkerboard, place a positive integer.
The values in each column of the checkerboard must be in strictly increasing order from
top to bottom, and the values in each row of the checkerboard must be in strictly
increasing order from left to right.

1   2   3   4
3   4   5   6
5   6   7   8
7   8   9   10

A Magic Checkerboard has an additional constraint. The cells that share only a corner must
have numbers of different parity (Even vs Odd). Note that the following checkboard is invalid,
because 2 and 4 share only a corner and have the same parity:

1   2
4   6

The first 4 x 4 example is a valid Magic Checkboard. Given a partially filled magic checkboard, can you
fill the remaining locations on the checkboard, so that the sum of all values is as small as possible?

Input
Each input will consist of a single test case. Note that your program may be run multiple times on different inputs.
Each input starts with a line with two space-separated integers n and m (1 <= n, m <= 2000), representing the number
of rows (n) and the number of columns (m) of the checkerboard. Each of the next n lines will contain m space-separated
integers c (0 <= c <= 200), representing the contents of the checkerboard. Zero is used for cells without numbers that
you must fill in. You may use any positive integers to fill in the cells without numbers, so long as you form a valid
Magic Checkerboard. You are not limited to numbers <= 2000, and the numbers are not required to be unique.

Output
Output a single integer representing the minimum sum possible by replacing the 0 cells with positive integers to form a
valid Magic Checkerboard. Output -1 if it is not possible to replace the 0 cells to meet the constraints of a Magic Checkerboard.
"""

def fill_magic_checkerboard(n, m, board):
    # Function to check if a value is valid for a cell
    def is_valid_value(val, i, j):
        if i > 0 and j > 0:
            return val % 2 != board[i-1][j] % 2 and val % 2 != board[i][j-1] % 2
        return True

    # Fill the board
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                possible_values = [val for val in range(1, n * m + 1) if is_valid_value(val, i, j)]
                if not possible_values:
                    return -1
                board[i][j] = min(possible_values)

    # Check the parity constraint for corner neighbors
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] % 2 == board[i-1][j] % 2 and board[i][j] % 2 == board[i][j-1] % 2:
                return -1

    # Calculate the sum
    return sum(sum(row) for row in board)

# Input
n, m = map(int, input().split())
board = []
for _ in range(n):
    row = list(map(int, input().split()))
    board.append(row)

# Fill the checkerboard and calculate the minimum sum
min_sum = fill_magic_checkerboard(n, m, board)

# Output
print(min_sum)