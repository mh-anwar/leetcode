# 3115. Maximum Prime Difference (Contest 393)
# 2024-04-13

# Approach - Beats 5.02% 
# Loop through the numbers in the array check if each is prime, append to an array if it is
# Return the maximum distance.

# Complexity
# Time: Unsure

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def isPrime(main):
            if main == 1:
                return False
            for i in range(2, main):
                if main % i == 0:
                    return False
            return True
        
        newNums = []
        # first determine if prime
        for i in range(len(nums)):
            numIsP = isPrime(nums[i])
            if numIsP:
                newNums.append(i)
        
        return newNums[-1] - newNums[0]