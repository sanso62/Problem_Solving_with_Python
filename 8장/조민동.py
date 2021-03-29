# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_deque: Deque = collections.deque()
        
        if not head:
            return True
        
        while head:
            head_deque.append(head.val)
            head=head.next
        
        for i in range(len(head_deque)//2):
            if head_deque.popleft()!=head_deque.pop(): 
                return False
        
        return True
