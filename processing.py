import numpy as np
import csv
import minizinc as mzn
from pathlib import Path
import time
import argparse


def setup_mzn(path_to_mzn_executable, solver_name) :
    driver = mzn.driver.Driver(Path(path_to_mzn_executable))
    driver.make_default()
    sudoku_model = mzn.Model('./model.mzn')
    solver = mzn.Solver.lookup(solver_name)
    instance = mzn.Instance(solver, sudoku_model)
    return sudoku_model, solver, instance

def parse_grid(grids, index):
    grid = np.empty((9, 9), dtype=int)
    for i, num in enumerate(grids[index][1]):
        row = i//9
        col = i - 9*row
        grid[row, col] = num
    return grid

def main() :
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="Index of the grid", type=int) 
    parser.add_argument("--mzn_path", help="Path to minizinc executable", default='/snap/bin/minizinc') 
    parser.add_argument("--solver", help="Name of the solver to use", default='gecode') 
    
    args = parser.parse_args()

        
    model, solver, instance = setup_mzn(args.mzn_path, args.solver)

    with open('sudoku.csv') as f :
        grids = list(csv.reader(f))
        if args.index <=0 or args.index > len(grids) :
            print(f"Index must be between 1 and {len(grids)}")
            exit(1)
        instance['grid'] = parse_grid(grids, args.index)

    st = time.time()
    result = instance.solve()
    dur = time.time() - st

    print(np.array(result["grid_solution"]))
    print(f'Solved the grid in {round(dur*1000,1)} ms')


if __name__ == '__main__' : main()