def arrayPairSum(self, nums: List[int]) -> int:
	even_index_sum=0
	nums.sort()
	for i in range(len(nums)//2):
		even_index_sum+=nums[2*i]
	return even_index_sum
