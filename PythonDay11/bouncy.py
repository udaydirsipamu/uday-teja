def bouncy(n):
    n_str=str(n)
    return n_str!=''.join(sorted(n_str)) and n_str!=''.join(sorted(n_str,reverse=True))
n=int(input("Enter a number:"))
if n<100:
    print("Cannot be a bouncy number")
elif bouncy(n):
    print(n,"is a Bouncy number")
else:
    print(n,"is not a Bouncy number")