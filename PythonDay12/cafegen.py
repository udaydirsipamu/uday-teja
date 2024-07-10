class cafe:
    def __init__(self,name):
        self.name=name
    def __iter__(self):
        for item in self.name:
            yield item
c=cafe(["Ali cafe","Nilofar cafe","Deccan cafe"])
for i in c:
    print(i)
for i in c:
    print(i)