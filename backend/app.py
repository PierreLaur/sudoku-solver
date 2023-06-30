from flask import Flask, jsonify, request
from solver import solve

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(message=f"hey, it's backend!")


@app.route("/solve", methods=["POST"])
def call_solve():
    grid = request.json["grid"]
    # Pre-process the grid
    for r in range(9):
        for c in range(9):
            if not grid[r][c] or grid[r][c] not in "123456789":
                grid[r][c] = 0
            else:
                grid[r][c] = int(grid[r][c])
    solution, status = solve(grid)
    if solution:
        for i in range(9):
            solution[i] = [str(solution[i][j]) for j in range(9)]
    return jsonify(grid=solution, status=status)


if __name__ == "__main__":
    app.run(debug=True)
