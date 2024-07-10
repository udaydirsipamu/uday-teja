def enumNPrint(mystr):
    words=[]
    linec,i,size=1,0,len(mystr)
    curr_word=""
    while i<size:
        if mystr[i] == ' ':
            if curr_word:
                words.append(f'{linec}. {curr_word}')
                curr_word=""
                linec+=1
        else:
            curr_word+=mystr[i]
        i+=1
    if curr_word:
        words.append(f'{linec}. {curr_word}')

    return words
mystr="This is a lengthy string here"
words=enumNPrint(mystr)
print(words)