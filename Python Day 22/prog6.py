def cyclic_number(n):
    n_str=str(n)
    l=len(n_str)
    for i in range(1,l+1):
        if sorted(str(n*i))!=sorted(n_str):
            return False
    return True
n=int(input("Enter number:"))
if cyclic_number(n):
    print("It is a cyclic number")
else:
    print("Not a cyclic number")