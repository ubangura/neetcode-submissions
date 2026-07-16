from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        WATER, TREASURE, LAND, INF = -1, 0, 2147483647, 2147483647
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Iterate matrix
            # Append cells of treasure to queue
        queue = deque()

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == TREASURE:
                    queue.append((x, y, 0))
        
        # Multi-source BFS
        while queue:
            level = len(queue)

            for cell in range(level):
                x, y, dist = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x , new_y = x + dx, y + dy

                    if (0 <= new_x < ROWS
                    and 0 <= new_y < COLS
                    and grid[new_x][new_y] == LAND):
                        grid[new_x][new_y] = dist + 1
                        queue.append((new_x, new_y, dist + 1))
            
        