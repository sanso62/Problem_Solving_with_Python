nums = [2,7,11,19]
target = 9

for i in range(len(nums)):
    for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                    print([i,j])
