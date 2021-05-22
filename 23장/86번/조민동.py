class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray=[0]*len(nums)
        sum_subarray=[]
        for i in range(len(nums)):
            max_sum=nums[i]
            for j in range(i+1):
                subarray[j]+=nums[i]
                if subarray[j]>max_sum:
                    max_sum=subarray[j]
            sum_subarray.append(max_sum)
                
        
        return max(sum_subarray)
