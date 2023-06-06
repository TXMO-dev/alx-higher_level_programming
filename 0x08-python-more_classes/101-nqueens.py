#!/usr/bin/python3
import sys
"""
This is the rect  module.

This module provides a  Rectangle class.
"""

def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    """
    Recursive function to solve the N Queens problem using backtracking
    """
    # Base case: If all queens are placed, print the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_nqueens(board, col + 1)

            # Backtrack: If placing queen in board[i][col] doesn't lead to a solution, remove the queen from board[i][col]
            board[i][col] = 0

    return False

# Check if the number of arguments is correct
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Check if N is an integer
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

# List to store all solutions
solutions = []

# Solve the N Queens problem
solve_nqueens(board, 0)

# Print all solutions
for solution in solutions:
    print(solution)
