def swap_n(a,b):
    a=a ^ b
    b=a ^ b
    a=a ^ b
    return a,b
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=swap_n(a,b)
print("After swapping\n")
print(a)
print(b)