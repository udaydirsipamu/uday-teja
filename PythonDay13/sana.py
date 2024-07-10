def anag(w1,w2):
    return sorted(w1.lower())==sorted(w2.lower())
def find_anag(s):
    w=s.split()
    anagrams=[]
    for i in range(len(w)):
        for j in range(i+1,len(w)):
            if anag(w[i],w[j]):
                anagrams.append(w[i])
                anagrams.append(w[j])
    return set(anagrams)
s=input("Enter a string")
anagrams=find_anag(s)
print(" ".join(anagrams))