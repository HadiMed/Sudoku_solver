import numpy as np 

sudoku_grid= [[0, 1, 9, 0, 6, 0, 5, 4, 0]
,[0, 0, 0, 0, 0, 0, 0, 0, 0]
,[8, 2, 0, 9, 7, 4, 0, 3, 6]
,[0, 0, 1, 5, 0, 3, 8, 0, 0]
,[0, 0, 0, 0, 0, 0, 0, 0, 0]
,[0, 0, 2, 7, 0, 1, 6, 0, 0]
,[7, 5, 0, 1, 3, 8, 0, 9, 2]
,[0, 0, 0, 0, 0, 0, 0, 0, 0]
,[0, 8, 3, 0, 4, 0, 7, 1, 0]
]
k=0


def possible(sudoku_grid,number,x,y):
    for i in range(9):
        if number==sudoku_grid[i][y] or number==sudoku_grid[x][i]:
            return False
    
    square=[int(x/3),int(y/3)]

    first_position_in_square=[square[0]*3,square[1]*3]

    for x in range(0,3):
        for y in range(0,3):
            if sudoku_grid[x+first_position_in_square[0]][y+first_position_in_square[1]]==number:
                return False
    return True 


def solve():
    global k 
    global sudoku_grid  
    for x in range(9):
        for y in range(9):

            if sudoku_grid[x][y]==0:
                for n in range(1,10):
                    if possible(sudoku_grid,n,x,y):
                        sudoku_grid[x][y]=n
                        solve()
                        if k==1:
                            return
                        sudoku_grid[x][y]=0
                        
                return 
    for x in sudoku_grid:
        print(x)
    
    k=1 
    
data=solve()
print("\n\n")
for x in sudoku_grid:
    print(x)
    





