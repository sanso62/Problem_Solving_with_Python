class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_multi=1
        result=[0 for i in range(len(nums))]
        n_zero=0
        for num in nums:
            if num!=0: all_multi*=num
            else: n_zero+=1
        print(all_multi)
        
        for i, num in enumerate(nums):
            if n_zero>1: return result
            elif n_zero==1:
                if num==0:
                    result[i]=all_multi
                    return result
                continue
            result[i]=all_multi//num
        
        return result
