# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list = []
        for list in lists:
            while list:
                sorted_list.append(list.val)
                list = list.next
        sorted_list = sorted(sorted_list)
        
        dummy = cur = ListNode()
        for i in sorted_list:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next
