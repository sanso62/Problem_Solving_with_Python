class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n sub each element
        sub_target_nums=[target-num for num in nums]
        print(sub_target_nums)
        # zip
        zip_nums=[sorted(n) for n in zip(nums, sub_target_nums)]
        print(zip_nums)
        # check
        result=collections.defaultdict(list)
        for i in range(len(nums)):
            result[tuple(zip_nums[i])].append(i)
        print(result)
        for val in result.values():
            if len(val)==2: return val
