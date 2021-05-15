class Solution:
	def rob(self, nums: List[int]) -> int:
		used, notUsed=[0]*len(nums), [0]*len(nums)

		for i in range(len(nums)):
			for j in range(i-1):
				used[i]=max(used[i],used[j])
			for j in range(i):
				used[i]=max(used[i],notUsed[j])
				notUsed[i]=max(used[i],used[i-1])
			used[i]+=nums[i]

		return max(used[len(nums)-1],notUsed[len(nums)-1])
