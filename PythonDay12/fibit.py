class Fibonacci:
    def __init__(self,n):
        self.n=n
        self.curr=0
        self.next=1
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count>=self.n:
            raise StopIteration
        else:
            res=self.curr
            self.curr,self.next=self.next,self.curr+self.next
            self.count+=1
            return res
n=int(input())
fibonacci=Fibonacci(n)
for i in fibonacci:
    print(i)