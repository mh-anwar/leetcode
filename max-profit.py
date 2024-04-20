# 121. Best Time to Buy and Sell Stock (Grind75 #4) - UNSOLVED
# 2024-04-19

# Approach
# First attempt TLE'd with O(n^2)

# Complexity
# Time: O(n^2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > maxProf:
                    maxProf = prices[j] - prices[i]
        return maxProf