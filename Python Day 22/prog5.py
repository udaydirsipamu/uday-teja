def sum_divisors(n):
    div_sum=1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i==(n//i):
                div_sum+=i
            else:
                div_sum+=(i+ n // i)
    return div_sum
def amicable(n1,n2):
    return sum_divisors(n1)==n2 and sum_divisors(n2)==n1
n1=int(input("Enter first number:"))
n2=int(input("Enter 2nd number:"))
if amicable(n1,n2):
    print("Two numbers are Amicable numbers")
else:
    print("Not amicable numbers")