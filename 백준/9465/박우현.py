T=int(input())

for t in range(T):
    sticker=[[],[]]
    total=[]
    maxscore=0

    n=int(input())
    sticker[0]=list(map(int,input().split()))
    sticker[1]=list(map(int,input().split()))

    total.append([0]*n)
    total.append([0]*n)

    for j in range(n):
        for i in range(2):
            if j==0:
                total[i][j]=sticker[i][j]
            elif j==1:
                total[i][j]=sticker[i][j]+total[(i+1)%2][j-1]
            else:
                total[i][j]=sticker[i][j]+max(total[(i+1)%2][j-1],total[0][j-2],total[1][j-2])
            maxscore=max(maxscore,total[i][j])

    print(maxscore)
