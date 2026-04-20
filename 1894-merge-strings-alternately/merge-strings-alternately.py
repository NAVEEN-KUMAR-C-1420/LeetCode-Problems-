class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res=""
        i,j=0,0
        while i<len(w1) and j<len(w2):
            res+=w1[i]
            res+=w2[j]
            i+=1
            j+=1
        while i<len(w1):
            res+=w1[i]
            i+=1
        while j<len(w2):
            res+=w2[j]
            j+=1
        return res
