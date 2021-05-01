K=int(input())
stack=[]
stack.append(0)
sum=0

for i in range(K):
    number=int(input())

    if(number==0):
        stack.pop()
    else:
        stack.append(number)

for i in range(len(stack)):
    sum+=stack[i]

print(sum)
