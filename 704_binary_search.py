# 704. Binary Search (Grind75 #8)
# 2024-04-24

# Approach
# First attempt creates two pointers, one at the start, one at the end and splits the array - beats 48.89%
# in half, updating the start/end accordingly until the target is found, if not then return -1

# Second attempt is a recursive approach that gets the middle, checks if the target is the middle and returns - beats 80.81%
# if not, based on whether the target is greater than or less than the mid, the function returns itself with 
# the updated left/right. If the left and right pointers are the same, and the target is not found, return -1

class Solution:
    def biSearch(self, arr, target, left, right):
        if left <= right:
            mid = (right + left)//2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                return self.biSearch(arr, target, mid + 1, right)
            elif target < arr[mid]:
                return self.biSearch(arr, target, left, mid - 1)
        else:
            return -1
    def search(self, nums: List[int], target: int) -> int:
        return self.biSearch(nums, target, 0, len(nums)-1)

# First attempt, iterative approach
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