a=[]
b=[]
for i in range(10) :
  a.append(int(input()))
  b.append(a[i]%42)
b1 = set(b)
print(len(b1))
