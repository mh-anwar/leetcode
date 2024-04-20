# 21. Merge Two Sorted Lists (Grind75 #3)
# 2024-04-19

# Approach
# Create an empty node, while both lists exist compare the current node values from both
# Take the node X with a lesser value and set it to the next in the empty node --> set the same node X to it's next node
# At the end if either list still has a value left, set it as the next and return the head of the list

# Complexity
# Time: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        main = ListNode()
        head = main
        # Side by side loop - required BOTH to exist
        while list1 and list2:
            # if the first list node is less, set as next element
            if list1.val < list2.val:
                main.next = list1
                main = list1
                list1 = list1.next
            else:
                main.next = list2
                main = list2
                list2 = list2.next
        # If any of the lists have a remaining node, set as last element
        if list1:
            main.next = list1
        else:
            main.next = list2
        return head.next
    

# First Attempt

"""         
def insertNode(node, listHead):
    if node.val < listHead.val:
        # Go to next
        return insertNode(node, listHead.next)
    elif node.val >= listHead.val:
        if node.val <= listHead.next.val:
            node.next = listHead.next
            listHead.next = node
            print(listHead)
            return listHead
            
def loopThru(node, firstList):
    if (node is not None) and (firstList is not None):
        print( firstList.val)
        firstList = insertNode(node, firstList)
        return loopThru(node.next, firstList)
    else:
        return firstList

if (list1 is not None) and (list2 is not None):
    final = loopThru(list2, list1)
    return final
return ListNode() 
"""