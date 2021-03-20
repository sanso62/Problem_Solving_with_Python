import collections

txt = input('입력 : ')
ban = input('ban : ')

wordlist = txt.lower().split()

for word in wordlist:
    if ban in word:
        wordlist.remove(word)

counts= collections.Counter(wordlist)
print(counts.most_common(1)[0][0])
