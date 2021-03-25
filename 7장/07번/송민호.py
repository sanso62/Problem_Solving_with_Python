def numplus (self, nums:List[int],target :int) :
    for i in (len(nums)):
        for j in (i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return[i,j]
