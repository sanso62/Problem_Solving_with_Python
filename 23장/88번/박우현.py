class Solution:
	def rob(self, nums: List[int]) -> int:
		used=[0]*len(nums)

		for i in range(len(nums)):
			for j in range(i-1):
				used[i]=max(used[i],used[j])
			used[i]+=nums[i]

		return max(used[len(nums)-1],used[len(nums)-2])
