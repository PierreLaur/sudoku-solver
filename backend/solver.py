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


def to_string(grid):
    """Creates a string representation of the grid"""
    result = ""
    for i in range(9):
        for j in range(9):
            result += str(grid[i][j]) + " "
            if j == 2 or j == 5:
                result += "| "
        result += "\n"
        if i == 2 or i == 5:
            result += "- " * 11 + "\n"

    return result


def solve(grid):
    model = cp_model.CpModel()

    digits = [[model.NewIntVar(1, 9, "") for j in range(9)] for i in range(9)]

    # Pre-fill the grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                model.Add(grid[i][j] == digits[i][j])

    for i in range(9):
        model.AddAllDifferent(digits[i])

    for j in range(9):
        model.AddAllDifferent([digits[i][j] for i in range(9)])

    # Digits in the same block must be different
    for r in range(3):
        for c in range(3):
            model.AddAllDifferent(
                [digits[3 * r + i][3 * c + j] for i in range(3) for j in range(3)]
            )

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print("No solution found")
        exit()

    solution = [[solver.Value(digits[i][j]) for j in range(9)] for i in range(9)]

    return solution


def main():
    index = int(sys.argv[1])
    grid = parse_grid(index)

    solution = solve(grid)

    print("Grid : ")
    print(to_string(grid))
    print("Solution : ")
    print(to_string(solution))


if __name__ == "__main__":
    main()
