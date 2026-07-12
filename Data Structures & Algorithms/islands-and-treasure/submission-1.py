from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # [0,-1],
        # [I,-1]

        ROWS, COLS = len(grid), len(grid[0])
        WATER, TREASURE, LAND, INF = -1, 0, 2147483647, 2147483647
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS
        def bfs(x, y, visited) -> int:
            queue = deque([(x, y, 0)])

            while queue:
                x, y, dist = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy
                    
                    if (0 <= new_x < ROWS
                    and 0 <= new_y < COLS
                    and (new_x, new_y) not in visited
                    and grid[new_x][new_y] != WATER):
                        if grid[new_x][new_y] is TREASURE:
                            return dist + 1

                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y, dist + 1))
            
            return INF

        # Iterate matrix
        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == LAND:
                    grid[x][y] = bfs(x, y, set())