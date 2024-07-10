def w_to_dig(s):
    w_to_dig_dict={"Zero":"0","One":"1","Two":"2","Three":"3","Four":"4","Five":"5","Six":"6","Seven":"7","Eight":"8","Nine":"9"}
    words=s.split()
    dig="".join(w_to_dig_dict.get(w,"") for w in words)
    return dig
s=input("Enter string:")
print(w_to_dig(s))