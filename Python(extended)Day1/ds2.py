def split_line(mystr):
    str1=mystr.split()
    for i,str1 in enumerate(str1,1):
        print(f"{i}. {str1}")
mystr="This is a lengthy string here"
split_line(mystr)