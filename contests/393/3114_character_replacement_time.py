# 3114. Latest Time You Can Obtain After Replacing Characters (Contest 393)
# 2024-04-13

# Approach - Beats 74.24% 
# 

# Complexity
# Time: O(n)

class Solution:
    def findLatestTime(self, s: str) -> str:
        num1 = s[0]
        num2 = s[1]
        num3 = s[3]
        num4 = s[4]
        
        # figure out which one's
        if num1 == "?":
            if num2 == "?":
                num1 = 1
            elif int(num2) <= 1:
                num1 = 1
            else:
                num1 = 0
                
                
        if num2 == "?":
            if num1 == "0":
                num2 = 9
            else:
                num2 = 1
                
        if num3 == "?":
            num3 = 5
            
        if num4 == "?":
            num4 = 9
        
        final = str(num1) + str(num2) + ":" + str(num3) + str(num4)
        return final