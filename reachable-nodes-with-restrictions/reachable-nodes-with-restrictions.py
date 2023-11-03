class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node, seen):
            seen[node] = True
            count = 1

            for neighbor in graph[node]:
                if not seen[neighbor]:
                    count += dfs(neighbor, seen)
            return count

        # Build graph
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = [ False ] * n
        for node in restricted:
            seen[node] = True

        return dfs(0, seen)
