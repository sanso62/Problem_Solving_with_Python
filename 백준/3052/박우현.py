remain=list()
count=0

for i in range(42):
    remain.append(False)
for i in range (10):
    num=int(input())
    remain[num%42]=True

for i in range (42):
    count+=remain[i]

print(count)
