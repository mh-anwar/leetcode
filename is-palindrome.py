# 125. Valid Palindrome (Grind75 #5)
# 2024-04-20

# Approach
# First attempt use two pointers to compare each letter from left to right - beats 10.53%
# Second attempt: clean string, split it in half and compare the two halves - beats 22.23%
# Third attempt: clean string, reverse it and compare with original - beats 51.54%
# Final attempt: clean string with RegEx, reverse and compare with original - beats 86.00% 

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Get rid of anything that is _not_ a-z, A-Z or 0-9
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        news = s[::-1]
        if news == s:
            return True
        return False
    
        # Third attempt - Clean out string, compare it with it's reverse
        newStr = ""
        for letter in s:
            if letter.isalnum() == True:
                newStr += str(letter.lower())
        if len(newStr) == 0:
            return True
        news = newStr[::-1]
        if news == newStr:
            return True
        return False

        # Second attempt - Clean out string, split in half, compare both halves
        # Time: O(n)
        newStr = ""
        for letter in s:
            if letter.isalnum() == True:
                newStr += str(letter.lower())
        l = len(newStr)
        if l == 0:
            return True
        s = newStr
        
        if l % 2 == 0:
            h = int(l/2)
            # first half
            f = newStr[:h]
            # next half
            n = newStr[h:][::-1]
            if f == n:
                return True
            return False
        else:
            # first half
            f = newStr[:int((l-1)/2)]
            # next half
            n = newStr[int((l+1)/2):][::-1]
            if f == n:
                return True
            return False
        
        # First attempt - Clean out string, start from left and right, compare each letter
        # Time: O(n)
        newStr = ""
        for letter in s:
            if letter.isalnum() == True:
                newStr += str(letter.lower())
        if len(newStr) == 0:
            return True
        l = 0
        r = len(newStr)-1

        while True:
            if (l == r) or (len(newStr)/2 == l):
                return True
            if str(newStr[l]) == str(newStr[r]):
                l += 1
                r -= 1
            else:
                return False
        return True