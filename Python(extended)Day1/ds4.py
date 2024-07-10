from splitterOne import mysplitter
def wtonum(mystr):
    temp,total=0,0
    numbers={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9 ,'ten':10, 
              'twenty':20,'thirty':30,'fourty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000,'lakh':100000,'crore':10000000}
    for word in mysplitter(mystr):
        if word in numbers:
            if numbers:
                if numbers[word]<100:
                    temp+=numbers[word]
                else:
                    temp*=numbers[word]
        if word in numbers:
            total+=temp
        return total
    if __name__ == '__main__':
        mystr='eighty nine lakh fifty four thousand and twenty five'
        print(f'{mystr} --> {wtonum(mystr)}')