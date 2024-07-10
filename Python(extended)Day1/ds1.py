def algoON(num):
    for _ in range(num):
        pass
def algoONpow2(num):
    for i in range(num):
        for j in range(num):
            pass
if __name__=='__main__':
    from sys import argv
    from time import perf_counter

    num=100

    if len(argv) == 2:
        num=int(argv[1])
    start=perf_counter()
    algoONpow2(num)
    end=perf_counter()
    print(f'Time taken: {round(end-start,3)} secs for num --> {num}')