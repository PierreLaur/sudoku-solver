import sys
import csv
from ortools.sat.python import cp_model


def parse_grid(index):
    """Reads the grid at the specified index in the sudoku.csv file and returns it as a list"""
    with open("sudoku.csv") as f:
        grids = list(csv.reader(f))
        if index <= 0 or index > len(grids):
            print(f"Index must be between 1 and {len(grids)}")
            exit(1)

    grid = [[0 for j in range(9)] for i in range(9)]
    for i, num in enumerate(grids[index][1]):
        row = i // 9
        col = i - 9 * row
        grid[row][col] = int(num)
    return grid


def solve(grid):
    model = cp_model.CpModel()

    digits = [[model.NewIntVar(1, 9, "") for j in range(9)] for i in range(9)]

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                model.Add(grid[i][j] == digits[i][j])

    for i in range(9):
        model.AddAllDifferent(digits[i])

    for j in range(9):
        model.AddAllDifferent([digits[i][j] for i in range(9)])

    for r in range(3):
        for c in range(3):
            model.AddAllDifferent(
                [digits[3 * r + i][3 * c + j] for i in range(3) for j in range(3)]
            )

    solver = cp_model.CpSolver()
    solver.parameters.subsolvers.extend(["core", "default_lp", "no_lp"])
    status = solver.Solve(model)

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        solution = [[solver.Value(digits[i][j]) for j in range(9)] for i in range(9)]
        status = 0
    else:
        solution = []
        status = 1

    return solution, status
