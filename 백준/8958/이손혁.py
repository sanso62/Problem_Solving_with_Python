num = int(input())

for i in range(num):
    s = 0 
    s_sum = 0
    q = input()
    for j in q:
        if j == 'O':
            s = s + 1
            s_sum = s_sum + s
        else:
            s = 0
            
    print(s_sum)
