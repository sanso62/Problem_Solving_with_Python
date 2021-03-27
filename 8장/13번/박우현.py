# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		palindrome=[]
		size=0

		if not head:
			return True

		while head!=None:
			palindrome.append(head.val)
			size+=1
			head=head.next

		for i in range(size//2):
			if palindrome[i]!=palindrome[size-1-i]:
				return False

		return True
