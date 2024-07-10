def min_max_freq(s):
    freq={}
    for char in s:
        if char.isalpha():
            char=char.lower()
            freq[char]=freq.get(char,0)+1
    min_char=min(freq,key=freq.get)
    max_char=max(freq,key=freq.get)
    return min_char,max_char
s=input("Enter string:")
min_char,max_char=min_max_freq(s)
print(f"Least frequency character:{min_char}:{s.count(min_char)}")
print(f"Maximun frequency character:{max_char}:{s.count(max_char)}")