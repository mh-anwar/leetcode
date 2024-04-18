# 1. Two Sum
# 2024-04-17

# Approach
# Loop through the array indices once, and for each index loop through the array again 
# to find the elements that sum up to the target; return the indices.

# Complexity
# Time: O(n^2)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]