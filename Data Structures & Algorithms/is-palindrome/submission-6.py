class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove whitespaces 
        word = s.replace(" ", "")
        word = ''.join(filter(str.isalnum, s))
        word = word.lower()
        print(word[::-1])
        return True if word == word[::-1] else False