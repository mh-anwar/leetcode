#  3131. Find the Integer Added to Array I (Contest 395)
# 2024-04-28

# Approach
# Sort both arrays, and because the difference is constant, return the difference 
# between first element in both arrays

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return 0
        nums1.sort()
        nums2.sort()
        
        return nums2[0] - nums1[0]