# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # print(len(lists), lists.count(None))
        if not lists or len(lists)==lists.count(None):
            return None
        
        lists_val=[]
        extra=[]
        for i in range(len(lists)):
            if lists[i]:
                lists_val.append((lists[i].val, i))

        lists_val.sort(reverse=True)    
        val, n=lists_val.pop()
        # print(val,n)
        lists[n]=lists[n].next

        node=ListNode(val)
        node.next=self.mergeKLists(lists)
        
        return node
