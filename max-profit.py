# 121. Best Time to Buy and Sell Stock (Grind75 #4)
# 2024-04-19

# Approach
# First attempt: TLE'd with O(n^2)
# Second attempt: use left and right pointers to find max profit - Beats 63.10%
# Third attempt: reverse loop through the stock prices, and only keep track of the maximum - Beats 81.61%
# anything less should be used to calculate the profit, if it's higher than the max profit then 
# set it as the max profit. Anything greater than the max price should be the new max price
# Time: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = prices[-1]
        prof = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] < maxPrice:
                newProfit = maxPrice - prices[i]
                prof = max(newProfit, prof)
            else:
                maxPrice = prices[i]
        return prof 

        # Second attempt - accepted, but not my solution
        # Time: O(n)
        l = 0
        r = 1 # always right of the left pointer
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l = r
            # Keep moving to the right to find another sol
            r += 1
        return maxProfit
    
        # First attempt - Brute force solution that exceeds time limit
        # Time: O(n^2)
        maxProf = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > maxProf:
                    maxProf = prices[j] - prices[i]
        return maxProf