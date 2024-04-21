# 3099. Harshad Number (Contest 391)
# 2024-03-30

# Approach - Beats 97.44%
# If x is more than one digit, convert to string, get the 0 and 1st index, convert to ints, and add them
# Otherwise only use x. Then divide the sum by the initial and return a result base don that

# Complexity
# Time: O(n)

class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        xstr = str(x)
        if len(xstr) > 1:
            sumOfDigits = int(xstr[0]) + int(xstr[1])
        else:
            sumOfDigits = int(xstr[0])
        
        if x%sumOfDigits == 0:
            return sumOfDigits
        else:
            return -1