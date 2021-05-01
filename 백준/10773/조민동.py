num=int(input())
stack=[]
for i in range(num):
    money=int(input())
    if money==0:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))
