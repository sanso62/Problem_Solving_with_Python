class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        for i in range(len(nums)-1):
            left, right =i, len(nums)-1
            result=[]
            while left<right-1:
                if nums[left] + nums[right]<=0:
                    m=right-1
                    while nums[left]+nums[right]+nums[m]>=0:
                        if nums[left]+nums[right]+nums[m]==0:
                            result.append((nums[left],nums[m],nums[right]))
                            break
                        m-=1
                    left+=1
                else:
                    m=left+1
                    while nums[left]+nums[right]+nums[m]<=0:
                        if nums[left]+nums[right]+nums[m]==0: 
                            result.append((nums[left],nums[m],nums[right]))
                            break
                        m+=1
                    right-=1
        for i in range(len(nums)-1):
            left, right = i, len(nums) - 1
            while left<right-1:
                if nums[left] + nums[right]<0:
                    m=right-1
                    while nums[left]+nums[right]+nums[m]>=0:
                        if nums[left]+nums[right]+nums[m]==0:
                            result.append((nums[left],nums[m],nums[right]))
                            print(left, m, right)
                            break
                        m-=1
                    left+=1
                else:
                    m=left+1
                    while nums[left]+nums[right]+nums[m]<=0:
                        if nums[left]+nums[right]+nums[m]==0: 
                            result.append((nums[left],nums[m],nums[right]))
                            print(left, m, right)
                            break
                        m+=1
                    right-=1
                
        result=[list(ele) for ele in set(result)]
        return result
