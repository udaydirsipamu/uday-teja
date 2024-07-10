def palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s ==s [::-1]
def count_vowels(s):
    s = s.lower()
    vowels='aeiou'
    return sum(1 for char in s if char in vowels)
