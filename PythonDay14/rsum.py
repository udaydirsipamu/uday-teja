print("Enter the elements row-wise:")
mat=[]
for _ in range(3):
    row=list(map(int,input().split()))
    mat.append(row)
r_sum=[sum(row) for row in mat]
c_sum=[sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
for i,r_sum in enumerate(r_sum):
    print(f"row{i+1}=",r_sum)
for j,c_sum in enumerate(c_sum):
    print(f"col{j+1}=",c_sum)

