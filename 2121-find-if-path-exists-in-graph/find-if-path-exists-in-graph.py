from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        if source==destination:
            return True
        visited=set()
        q=deque()
        visited.add(source)
        q.append(source)
        while q:
            node=q.popleft()
            if node==destination:
                return True
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        return False
