def ul_sum(matrix):
    u_sum=0
    l_sum=0
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            if j>=i:
                u_sum += matrix[i][j]
            if i>=j:

                l_sum += matrix[i][j]
    return u_sum,l_sum
print("Enter elements:")
matrix=[]
for _ in range(3):
    row=list(map(int,input().split()))
    matrix.append(row)
u_sum,l_sum=ul_sum(matrix)
print("Upper sum of traingle:",u_sum)
print("Loer sum of traingle is:",l_sum)