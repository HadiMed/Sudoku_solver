from flask import Flask , request , render_template
import solver
import numpy as np

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/handle_data",methods=['POST'])
def handle_data():
    data=request.form
    print(data)
    i=0
    grid=[]
    line=[]
    for x in data:
        if data[x]=='':
            line.append(0)
        else:
            line.append(int(data[x]))
        i+=1
        
        if i==9:
            
            grid.append(line)
            line=[]
            i=0
    print(np.matrix(grid))            
    solver.sudoku_grid=grid
    solver.k=0
    solver.solve()
    grid=solver.sudoku_grid

    print(grid)
    for x in grid:
        for y in x :
            if y==0:
                return render_template("index.html",warning="Please enter a valid sudoku grid!")
     
    
   
    return render_template("result.html",grid=grid)

app.run()