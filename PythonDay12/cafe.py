class cafe:
    def __init__(self,names):
        self.names=names
        self.i=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.i+=1
        if self.i<len(self.names):
            return self.names[self.i]
        raise StopIteration
c=cafe(["Ali cafe","Nilofar cafe","Deccan cafe"])
for i in c:
    print(i)