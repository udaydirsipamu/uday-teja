def identity(mat):
    n=len(mat)
    for i in range(n):
        for j in range(n):
            if i==j and mat[i][j]!=1:
                return False
            elif i!=j and mat[i][j]!=0:
                return False
    return True
mat=[[1,0,0],
     [0,1,0],
     [0,0,1]]
if identity(mat):
    print("Matrix is identity matrix")
else:
    print("Matrix is not ientity matrix")