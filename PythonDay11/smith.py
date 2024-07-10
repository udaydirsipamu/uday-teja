def smith(n):
    def prime_factors(n):
        f=[]
        div=2
        while n>1:
            while n%div==0:
                f.append(div)
                n//=div
            div+=1
        return f
    dig_sum=sum(int(dig) for dig in str(n))
    prime_factor_sum=sum(sum(int(dig) for dig in str(fa)) for fa in prime_factors(n))
    return dig_sum==prime_factor_sum
n=int(input("Enter a number:"))
if smith(n):
    print(n,"is a smith number")
else:
    print(n,"is not a smith number")
smith_numbers=[x for x in range(100,2001) if smith(x)]
print(smith_numbers)