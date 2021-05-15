class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		sum, maxValue = 0, nums[0]

		for i in range(len(nums)):
			sum+=nums[i]
			sum=max(sum,nums[i])
			maxValue=max(maxValue,sum)

		return maxValue
