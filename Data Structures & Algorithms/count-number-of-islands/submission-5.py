from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND = "0", "1"
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        # BFS
        def bfs(x, y) -> None:
            queue = deque([(x, y)])

            while queue:
                x, y = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy

                    if (0 <= new_x < ROWS
                    and 0 <= new_y < COLS
                    and grid[new_x][new_y] == LAND):
                        grid[new_x][new_y] = WATER
                        queue.append((new_x, new_y))

        # Iterate over matrix
            # If reach land
                # Increment num_islands
                # Run BFS on cell
                    # Mark cells visited (change value to "0")
        num_islands = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == LAND:
                    grid[x][y] = WATER
                    num_islands += 1
                    bfs(x, y)

        # return num_islands
        return num_islands