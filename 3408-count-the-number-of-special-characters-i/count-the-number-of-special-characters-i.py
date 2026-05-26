class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        lower=[i for i in word if i.isupper()]
        print(lower)
        c=0
        for i in set(lower):
            if i.lower() in word:
                c+=1
        return c