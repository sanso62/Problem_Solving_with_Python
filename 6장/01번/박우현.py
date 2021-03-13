string=str(input())
palindrome=True
start=0
end=len(string)-1

while start<end:
    if string[start]!=string[end]:
        palindrome=False
        break
    start+=1
    end-=1

print(palindrome)
