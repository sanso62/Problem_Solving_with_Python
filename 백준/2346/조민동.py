
n=int(input())
nums=list(map(int, input().split()))
nums=[(i+1, num) for i, num in enumerate(nums)]

result=[]
rm_i=nums[0][1]
number=nums[0][0]
# nums.pop(0)
while len(nums)>1:
    result.append(number)
    nums=[j for j in nums if j[0]>=number] + [k for k in nums if k[0]<number]
    _, rm_i= nums[0]
    number=nums[rm_i][0]
    nums.pop(0)

result.append(number)
   

for a in result:
    print(a, end=" ")
