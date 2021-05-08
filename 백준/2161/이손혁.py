n=int(input())
card = [i for i in range(1,n+1)] 
trash = [] #

while len(card) >1: 
    trash.append(card.pop(0)) 
    card.append(card.pop(0)) 

for i in trash:
    print(i,end=' ')

print(card[0])
