import numpy as np
def diagonal(mat):
    major_sum=np.trace(mat)
    minor_sum=np.trace(np.fliplr(mat))
    return major_sum,minor_sum
#rows=int(input())
#col=int(input())
#mat=np.array(input().split()).reshape(3,3)
mat=[[10,20,30],
     [40,50,60],
     [70,80,90]]
major_sum,minor_sum=diagonal(mat)
print("Sum of major diagonal is:",major_sum)
print("Sum of minor diagonal is:",minor_sum)