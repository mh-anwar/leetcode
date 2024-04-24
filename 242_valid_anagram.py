# 242. Valid Anagram (Grind75 #7)
# 2024-04-23

# Approach
# First attempt converts t into a list, and checks if all the letters in s are in t - beats 5.20%
# if any letter in s is not in t it immediately returns false, otherwise it removes that letter
# at the end if any letters remain in t return false, otherwise return s

# Second attempt checks if the length of the two is the same, if not returns false - beats 28.31%
# then returns whether the sorted s and sorted t are the same, which is the answer

# Third attempt initially meant to convert both s and t to dicts, then compare the dicts - beats 81.24%
# then the conversion of s and to dicts was done by `Collections.counter()` and compared

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # this line is completely useless, barely changes time
            return False
        
        ls = Counter(s)
        lt = Counter(t)

        if lt == ls:
            return True
        return False
    
        # Alternative to using counter, because importing libraries feels like cheating - beats 63.99%
        if len(s) != len(t):
            return False
            
        ls = {}
        lt = {}
        for i in range(len(s)):
            ls[s[i]] = ls.get(s[i], 0) + 1 # the second parameter is returned if the key is not found
            lt[t[i]] = lt.get(t[i], 0) + 1

        if lt == ls:
            return True
        return False
    
        # Second attempt
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t) # using sorted feels like cheating
    
        # First attempt 
        t = list(t)
        for i in s:
            if i in t:
                t.pop(t.index(i))
            else:
                return False
        if len(t) > 0:
            return False
        return True