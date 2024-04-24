# 226. Invert Binary Tree (Grind75 #6)
# 2024-04-22

# Approach
# First attempt uses a recursive approach, but is gloated - beats 56.16%
# Second attempt was to use the provided function itself as the recursive function - beats 76.45%
# it continiously calls itself with the left and right nodes and then switches them 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        l, r = root.left, root.right # I think this can be combined with the next line
        root.left, root.right = r, l
         
        return root

        # First attempt, create another function inside, and use it for recursion, operates similiar to above sol
        def invert(ele):
            if ele:
                l = ele.left
                r = ele.right
                ele.left = r
                ele.right = l
                return invert(ele.left), invert(ele.right)
            else:
                return
        
        invert(root)
        return root