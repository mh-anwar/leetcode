# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray (Contest 392)
# 2024-04-06

# Approach - Beats 93.44% 
# Loop through array, then loop through array from that index onwards and track longest increasing subarray until it stops
# Do the same and tracking longest decreasing subarray, compare the two and return the longest of either

# Complexity
# Time: O2(n^2)

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestLen = 1
        
        for i in range(len(nums)):
            # We get our first number, check if the next numbers are increasing/decreasing
            prevIndex = nums[i]
            currLongestLenInc = 1
        
            for j in range(i+1, len(nums)):
                currIndex = nums[j]
                
                if currIndex > prevIndex:
                    prevIndex = currIndex
                    currLongestLenInc += 1
                    continue
                else:
                    break
            if currLongestLenInc > longestLen:
                    longestLen = currLongestLenInc
        for i in range(len(nums)):
            # We get our first number, check if the next numbers are increasing/decreasing
            prevIndex = nums[i]
            currLongestLenDec = 1
        
            for j in range(i+1, len(nums)):
                currIndex = nums[j]
                
                if currIndex < prevIndex:
                    prevIndex = currIndex
                    currLongestLenDec += 1
                    continue
                else:
                    break
            
            if currLongestLenDec > longestLen:
                    longestLen = currLongestLenDec
        return longestLen