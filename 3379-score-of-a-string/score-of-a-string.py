class Solution:
    def scoreOfString(self, s: str) -> int:
        l=[]
        for i in s:
            l.append(ord(i))
        s=0
        for i in range(len(l)-1):
            s+=abs(l[i]-l[i+1])
        return s