def fs(n):
    con=str(n)+str(n*2)+str(n*3)
    dig=set(con)
    return len(con) == 9 and len(dig) == 9 and '0' not in dig
n=int(input("Entera number:"))
if fs(n):
    print(n,"is a Fascinating number")
else:
    print(n,"is not a Fascinating number")