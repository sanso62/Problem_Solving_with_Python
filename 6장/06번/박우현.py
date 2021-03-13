string=str(input())
max_start=0
max_end=0

for i in range(len(string)):
    for j in range(i,len(string)):
        start=i
        end=j
        palindrome=True

        while start<end:
            if string[start]!=string[end]:
                palindrome=False
                break
            start+=1
            end-=1
        if palindrome:
            if j-i>max_end-max_start:
                max_end=j
                max_start=i
                
print(string[max_start:max_end+1])
