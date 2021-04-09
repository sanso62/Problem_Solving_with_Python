# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def next(node, l1, l2):
            if l1==None and l2!=None:
                node=l2
                return node
            elif l2==None and l1!=None:
                node=l1
                return node
            elif l1==None and l2==None:
                return node

            if l1.val<=l2.val: 
                node, l1=l1, l1.next
            else: 
                node, l2=l2, l2.next
            
            node.next=next(node, l1, l2)
            return node

        init_node=None

        return next(init_node, l1, l2)
