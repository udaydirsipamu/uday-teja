def pell(n):
    prev=0
    curr=1
    print(prev,curr,end=" ")
    for i in range(2,n):
        nxt=2*curr+prev
        print(nxt,end=" ")
        prev=curr
        curr=nxt
n=int(input("Enter number"))
pell(n)