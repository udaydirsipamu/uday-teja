class Armstrong:
    def __init__(self,start=100,end=1000):
        self.start=start
        self.end=end
    def __iter__(self):
        for n in range(self.start,self.end):
            if self.arm(n):
                yield n
    def arm(self,n):
        dig_sum=sum(int(dig)**3 for dig in str(n))
        return dig_sum==n
arm_n=Armstrong()
for n in arm_n:
    print(n)