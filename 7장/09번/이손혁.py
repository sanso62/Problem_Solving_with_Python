nums = [-1, 0, 1, 2, -1, -4]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if j == i:
            False
        for x in range(j+1,len(nums)):
            if x == j:
                False
            if nums[i] + nums[j] + nums[x] == 0:
                print(nums[i],nums[j],nums[x])
               
# 실패함 중복 되는것 제외 실패.
