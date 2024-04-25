# 704. Binary Search (Grind75 #8)
# 2024-04-24

# Approach
# First attempt creates two pointers, one at the start, one at the end and splits the array - beats 48.89%
# in half, updating the start/end accordingly until the target is found, if not then return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -1
        while start <= end:
            middle = int((start + end)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle -1
            else:
                start = middle +1
        return -1