class Solution:
    def rob(self, nums: List[int]) -> int:
        subarray_sum=[]
        if len(nums)==1 or len(nums)==2:
            return max(nums)
        for i in range(2, len(nums)):
            subarray_sum.append(sum(nums[::i]))
            subarray_sum.append(sum(nums[1::i]))
            print(subarray_sum)
        
        return max(subarray_sum)
