class Solution:
    def totalNQueens(self, n: int) -> int:
        count=0
        def backtrack(r):
            nonlocal count
            if r==n:
                count+=1
                return
            for c in range(n):
                if c in col or r+c in pos or r-c in neg:
                    continue
                board[r][c]="Q"
                col.add(c)
                pos.add(r+c)
                neg.add(r-c)
                backtrack(r+1)
                board[r][c]="."
                col.remove(c)
                pos.remove(r+c)
                neg.remove(r-c)
        board=[["."]*(n)for _ in range(n)]
        col=set()
        pos=set()
        neg=set()
        backtrack(0)
        return count
