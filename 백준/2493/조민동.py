num=int(input())
tops=[int(input()) for _ in range(num)]

tops.reverse()
stack=[]
result=[0 for i in range(num)]

for i,top in enumerate(tops):
    if i==0:
        stack.append((i,top))
        continue

    while stack and stack[-1][1]<top:
        result[stack[-1][0]]=len(tops)-i
        stack.pop()

    stack.append((i, top))

result.reverse()
print(result)
