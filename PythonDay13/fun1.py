def fd(f):
    def mfun(*a):
        print("Welcome")
        f(*a)
        print("TY")
    return mfun
@fd
def fn1():
    print("Wipro session")
@fd
def fn2():
    print("Python session")
@fd
def fn3(a,b):
    print(a*b)

    fn1()
    fn2()
    fn3(3,4)