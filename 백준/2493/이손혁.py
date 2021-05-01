num = int(input())
stack = []
result = [0] * num
tower = list(map(int,input().split()))
for i in range(num-1, -1, -1):
    while stack and tower[stack[-1]] <= tower[i]:
        result[stack.pop()] = i+1
    stack.append(i)
st = str(result)
print(st)

import re
s = re.sub('[-=.#/?:$}]', '', st)
print(s)
