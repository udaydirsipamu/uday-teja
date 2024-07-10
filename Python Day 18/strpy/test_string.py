import string1
import pytest
def test_palindrome():
    assert palindrome("A man a plan a canal Panama")
    assert not palindrome("hello")
    assert palindrome("Nolemon,no melon")
    assert palindrome("")
def test_count_vowels():
    assert count_vowels("hello")==2
    assert count_vowels("world")==1
    assert count_vowels("AEIOU")==5
    assert count_vowels("xyz")==0
    assert count_vowels("")==0