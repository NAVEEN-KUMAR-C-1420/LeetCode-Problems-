class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:
        c.sort()
        res=[]
        def bt(start,curr,rem):
            if rem==0:
                res.append(curr[:])
                return
            if rem<0:
                return
            for i in range(start,len(c)):
                if i>start and c[i]==c[i-1]:
                    continue
                curr.append(c[i])
                bt(i+1,curr,rem-c[i])
                curr.pop()
        bt(0,[],target)
        return res
