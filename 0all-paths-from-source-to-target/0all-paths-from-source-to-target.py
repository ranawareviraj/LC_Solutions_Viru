class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def backtrack(source, target, current_path):
            if (source == target):
                all_paths.append(current_path[ : ])
                return
            
            for neighbor in graph[source]:
                current_path.append(neighbor)
                backtrack(neighbor, target, current_path)
                current_path.pop()
                
        all_paths = []
        n = len(graph)
        backtrack(0, n - 1, [ 0 ])
        return all_paths
        