l=[11,13,19,20,25,30]
even=list(filter(lambda x:x%2==0,l))
print(even)
double=list(map(lambda x:x*2,even))
print(double)