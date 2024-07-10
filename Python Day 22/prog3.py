def pattern3(n):
    for i in range(2,n+2,2):
        for j in range(10,10-i,-2):
            print(j,end=" ")
        print()
n=int(input("Enter no of lines:"))
pattern3(n)