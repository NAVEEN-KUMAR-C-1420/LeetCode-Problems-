class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen=set()
        count=0
        graph={}
        for i in range(len(isConnected)):
            graph[i]=[]
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        def dfs(node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)
        for n in graph:
            if n not in seen:
                seen.add(n)
                dfs(n)
                count+=1
        return count