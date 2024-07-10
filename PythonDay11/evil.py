def evil(n):
    binary=bin(n)[2:]
    c_ones=binary.count('1')
    return c_ones%2==0
n=int(input("Enter a number:"))
binary=bin(n)[2:]
c_ones=binary.count('1')
print("Input:",n)
print("Binary equivalent:",binary)
print("No of 1's:",c_ones)
if evil(n):
    print("Output:Evil number")
else:
    print("Output:Not an Evil number")