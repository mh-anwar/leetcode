# 3120. Count the Number of Special Characters I (Contest 394)
# 2024-04-21

# Approach
# Loop through each letter, save all letters that appear as uppercase, lowercase and aren't already stored
# Then increase the number of special chars. Return the number of special chars.

# Complexity
# Time: O(n)

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special = 0
        letters = []
        for i in word:
            if (i.upper() in word) and (i.lower() in word) and (i.upper() not in letters):
                letters.append(i.upper())
                special += 1
        return special