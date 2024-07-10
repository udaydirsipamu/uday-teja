def pattern2(n):
    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            print(2**j,end=" ")
        print()
n=int(input("Enter no of lines:"))
pattern2(n)