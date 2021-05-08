
N=int(input())
stack=[]
for i in range(1,N+1):
    stack.append(i)
while len(stack) != 1:
    stack.pop(0)
    stack.append(stack.pop(0))
print(stack)  
