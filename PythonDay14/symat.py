import numpy as np
def symmetric(mat):
    n=len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j]!=mat[j][i]:
                return False
    return True
#mat=np.array(input().split()).reshape(2,2)
mat=[[1,0],
     [0,1]]
if symmetric(mat):
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")