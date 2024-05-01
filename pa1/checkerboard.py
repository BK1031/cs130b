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

def is_valid(board, i, j, value):
    if any(board[i][col] == value for col in range(len(board[0]))):
        return False

    if any(board[row][j] == value for row in range(len(board))):
        return False

    neighbors = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for row, col in neighbors:
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] != 0 and board[row][col] % 2 == value % 2:
                return False
    return True

def recurse(board, i, j):
    if i == len(board):
        return True
    if j == len(board[0]):
        return recurse(board, i + 1, 0)
    if board[i][j] != 0:
        return recurse(board, i, j + 1)
    for value in range(1, 2001):
        if is_valid(board, i, j, value):
            board[i][j] = value
            if recurse(board, i, j + 1):
                return True
            board[i][j] = 0
    return False

def solve_magic_checkerboard(n, m, board):
    if n % 2 != 0 and m % 2 != 0:
        return -1
    if n % 2 != m % 2:
        return -1
    if not recurse(board, 0, 0):
        return -1
    return sum(sum(row) for row in board)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solve_magic_checkerboard(n, m, board))
