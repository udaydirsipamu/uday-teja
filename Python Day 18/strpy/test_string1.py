import string1
import pytest
def test_palindrome():
    assert string1.palindrome("A man a plan a canal Panama")==True
    assert string1.palindrome("hello")==False
    assert string1.palindrome("No lemon,no melon")==True
    #assert palindrome("")
def test_count_vowels():
    assert string1.count_vowels("hello")==2
    assert string1.count_vowels("world")==1
    assert string1.count_vowels("AEIOU")==5
    assert string1.count_vowels("xyz")==0
    assert string1.count_vowels("")==0