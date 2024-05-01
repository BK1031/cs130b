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

def is_valid(n, m, board):
    for row in range(n):
        for col in range(1, m):
            if board[row][col] <= board[row][col - 1]:
                return False
    for row in range(n - 1):
        for col in range(m - 1):
            if (board[row][col] % 2 == board[row + 1][col] % 2) and (board[row][col] != 0 and board[row + 1][col] != 0):
                return False
            if (board[row][col] % 2 == board[row][col + 1] % 2) and (board[row][col] != 0 and board[row][col + 1] != 0):
                return False
    return True

def solve(n, m, board):
    if n % 2 != m % 2:
        return -1

    for row in range(n):
        prev_value = 0
        for col in range(m):
            if board[row][col] == 0:
                for value in range(prev_value + 1, prev_value + 2 * n * m + 1):
                    board[row][col] = value
                    if is_valid(n, m, board):
                        break
                    board[row][col] = 0
                else:
                    return -1
            prev_value = board[row][col]

    return sum(sum(row) for row in board)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solve(n, m, board))
