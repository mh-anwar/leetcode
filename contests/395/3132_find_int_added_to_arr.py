#  3133. Find the Integer Added to Array II (Contest 395)
# 2024-04-28

# Approach
# This approach does not work, just a rough draft

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        print(nums1)
        print(nums2)
        
        cd = 0
        
        # not sliding window, but we are sliding a window
        # Start at a number, go through all the rest
        for i in range(len(nums1)):
            cd = nums2[0] - nums1[i]
            if i + len(nums2) < len(nums1):
                t = -1
                for j in range(i, i + len(nums2)):
                    t+=1
                    if nums2[t] - nums1[j] == cd:
                        continue
                    else:
                        cd = 0
                        break
                    
        return cd
                