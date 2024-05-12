#  100296. Permutation Difference between Two Strings (Contest 397)
# 2024-05-12

# Approach
# Loop through each letter in t and compare the difference to the letter's position in s. Store the difference and return

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i in range(len(t)):
            first_p = s.index(t[i])
            total += abs(first_p - i)
        return total