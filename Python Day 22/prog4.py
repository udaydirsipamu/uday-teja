def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(i-1,0,-1):
            print(j,end=" ")
        print()
n=int(input("Enter no of lines:"))
pattern4(n)