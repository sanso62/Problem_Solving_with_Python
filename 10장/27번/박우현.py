# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def mergeKLists(self, lists: List[ListNode]) -> ListNode:
		l=list()

		for i in range(len(lists)):
			while lists[i] is not None:
				l.append(lists[i].val)
				lists[i]=lists[i].next

		if len(l)==0:
			return None

		l.sort()

		LinkedList=ListNode()
		temp=LinkedList

		for i in range(len(l)):
			temp.val=l[i]
			if i<len(l)-1:
				temp.next=ListNode()
				temp=temp.next

		return LinkedList
