class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def bt(r):
            if r==n:
                copy=board[:]
                sol=[]
                for c in copy:
                    sol.append("".join(c[:]))
                ans.append(sol)
                return
            for c in range(n):
                if c in col or r-c in neg or r+c in pos:
                    continue
                board[r][c]="Q"
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                bt(r+1)
                board[r][c]="."
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)

        board=[["."]*n for _ in range(n)]
        ans=[]
        col=set()
        pos=set()
        neg=set()
        bt(0)
        return ans