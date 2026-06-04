class Solution:
    def combinationSum(self, c: List[int], target: int) -> List[List[int]]:
        res=[]
        def bt(idx,current):
            if sum(current)==target:
                res.append(current[:])
                return
            if idx>=len(c) or target<sum(current):
                return
            current.append(c[idx])
            bt(idx,current)
            current.pop()
            bt(idx+1,current)
        bt(0,[])
        return res