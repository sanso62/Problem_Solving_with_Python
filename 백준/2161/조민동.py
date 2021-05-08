num=int(input())

q=[n for n in range(1, num+1)]

while q:
    print(q.pop(0), end=" ")
    if not q:
        break
    q.append(q.pop(0))
