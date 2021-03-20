def productExceptSelf(self, nums: List[int]) -> List[int]:
	arr=[]
	mul=1
	zerocount=0

	for i in range(len(nums)):
		if nums[i]!=0:
			mul*=nums[i]
		else:
			zerocount+=1

	for i in range(len(nums)):
		if zerocount>1:
			arr.append(0)
		elif zerocount==1:
			if nums[i]==0:
				arr.append(mul)
			else:
				arr.append(0)
		else:
			arr.append(mul//nums[i])

	return arr
