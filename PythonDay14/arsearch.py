def se_ele(mat,target):
    for i,row in enumerate(matrix):
        for j,val in enumerate(row):
            if val==target:
                return i,j
    return None
print("Enter elements:")
matrix=[]
for _ in range(3):
    row=list(map(int,input().split()))
    matrix.append(row)
target=int(input("Enter element to search:"))
res=se_ele(matrix,target)
if res:
    print(f"Element {target} found at position:{res}")
else:
    print(f"Element {target} not found in the matrix")