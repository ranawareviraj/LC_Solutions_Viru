class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # DFS
        def dfs(start, visited_rooms):
            for neighbor in rooms[start]:
                if neighbor not in visited_rooms:
                    visited_rooms.add(neighbor)
                    # Add neighbor to BFS queue
                    dfs(neighbor, visited_rooms)
            return len(visited_rooms)

        # Return if we visited all rooms
        return dfs(0, { 0 }) == len(rooms)
