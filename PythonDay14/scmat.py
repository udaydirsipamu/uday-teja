def scalar(mat):
    n=len(mat)
    scalar_value=mat[0][0]
    for i in range(n):
        for j in range(n):
            if(i==j and mat[i][j]!=scalar_value) or (i!=j and mat[i][j]!=0):
                return False
    return True
mat=[[5,0,0],
     [0,5,0],
     [0,0,5]]
if scalar(mat):
    print("Matrix is Scalar matrix")
else:
    print("Matrix is not Scalar matrix")