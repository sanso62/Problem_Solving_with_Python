n = int(input())
numbers = [0,1]
if n == 1 :
    print(1)
elif n == 2 :
    print(2)
else :
    for i in range(2,n+1) :
        numbers.append(numbers[i-1]+numbers[i-2])
    print(numbers[n-1])   
