def prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,n//2,2):
        if n%i==0:
            return False
    return True
def circular_prime(n):
    n_str=str(n)
    if any(dig in n_str for dig in '024568'):
        return False
    for i in range(len(n_str)):
        if not prime(int(n_str)):
            return False
        n_str=n_str[1:]+n_str[0]
    return True
n=int(input("Enter a number:"))
if circular_prime(n):
    print("It is a circular prime")
else:
    print("It is not a circular prime")