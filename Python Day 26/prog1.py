def count_set_bits(n):
    c=0
    for i in range(1,n+1):
        while i:
            c+=i & 1
            i>>=1
    return c
n=int(input("Enter n:"))
print("Total set bits from 1 to ",n,":",count_set_bits(n))    