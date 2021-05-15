n = int(input())
idx = 0
result = []

ballon = list(map(int, input().split()))
index = [x for x in range(1, n + 1)]

temp = ballon.pop(idx)
result.append(index.pop(idx))

while ballon:
    if temp < 0:
        idx = (idx + temp) % len(ballon)
    else:
        idx = (idx + (temp - 1)) % len(ballon)
    temp = ballon.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end = ' ')
