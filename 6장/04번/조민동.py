class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #preprocessing
        paragraph=paragraph.lower()
        paragraph=re.sub("[\W_]", " ", paragraph)
        words=paragraph.split()
        print(words)
        #Counter
        counter_words=Counter(words)
        print(counter_words)
        for most_word in counter_words.most_common():
            if most_word[0] not in banned: return most_word[0]
