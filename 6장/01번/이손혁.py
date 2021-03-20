word = input("단어 입력 : ")

is_Palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-1 -i]:
        is_Palindrome = False
        break

print(is_Palindrome)
