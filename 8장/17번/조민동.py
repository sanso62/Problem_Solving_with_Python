# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node=head
        if not node:
            return node
        if not node.next:
            return node
        
        odd, even, next= node, node.next, node.next.next
        node, node.next, node.next.next = even, odd, self.swapPairs(next)
        
        return node
