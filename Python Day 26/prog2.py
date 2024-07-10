def even_odd(n):
    if n & 1==0:
        return "Even"
    else:
        return "Odd"
n=int(input("Enter n:"))
print(n,"is",even_odd(n))