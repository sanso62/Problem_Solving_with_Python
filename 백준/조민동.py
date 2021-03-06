n = int(input())
num_list=[0,1]
i=0
while i<n-1:
    num_list.append(num_list[-1]+num_list[-2])
    i+=1
if n==0: print(0)
else: print(num_list[-1])
