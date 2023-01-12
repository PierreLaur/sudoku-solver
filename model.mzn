array[1..9,1..9] of 0..9 : grid ;
array[1..9,1..9] of var 1..9 : grid_solution ;
constraint forall(i in 1..9, j in 1..9 where grid[i,j]>0)
            (grid_solution[i,j]=grid[i,j]) ;


include "alldifferent.mzn" ;
constraint forall(r in 1..9)(alldifferent(row(grid_solution,r))) ;
constraint forall(c in 1..9)(alldifferent(col(grid_solution,c))) ;

constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 1..3, j in 1..3])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 1..3, j in 4..6])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 1..3, j in 7..9])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 4..6, j in 1..3])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 4..6, j in 4..6])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 4..6, j in 7..9])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 7..9, j in 1..3])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 7..9, j in 4..6])) ;
constraint forall(block in 1..9)(alldifferent([grid_solution[i,j] | i in 7..9, j in 7..9])) ;

solve satisfy;

output["\(grid_solution[1,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[2,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[3,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[4,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[5,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[6,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[7,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[8,i]) " | i in 1..9] ++ ["\n"];  
output["\(grid_solution[9,i]) " | i in 1..9] ++ ["\n"];  