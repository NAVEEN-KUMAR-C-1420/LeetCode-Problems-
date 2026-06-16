class Solution:
    def processStr(self, s: str) -> str:
        res=""
        for i in s:
            if i.isalpha():
                res+=i
            elif i=="*":
                if len(res)==0:
                    continue
                else:
                    res=res[:len(res)-1]
            elif i=="#":
                res=res+res
            else:
                res=res[::-1]
        return res