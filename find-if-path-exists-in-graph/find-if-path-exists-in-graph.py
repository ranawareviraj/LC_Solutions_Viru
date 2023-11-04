class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node = source, target = destination, seen = set()):
            if node == target:
                return True
            seen.add(node)
            
            for neighbor in graph[node]:
                if neighbor not in seen:
                    if dfs(neighbor, target, seen):
                        return True
    
            return False
        
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        return dfs()
