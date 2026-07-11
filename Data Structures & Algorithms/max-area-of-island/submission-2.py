from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS
        def bfs(x, y) -> int:
            queue = deque([(x, y)])
            grid[x][y] = WATER
            count = 1

            while queue:
                x, y = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy

                    if (0 <= new_x < ROWS
                    and 0 <= new_y < COLS
                    and grid[new_x][new_y] is LAND):
                        grid[new_x][new_y] = WATER
                        queue.append((new_x, new_y))
                        count += 1
            
            return count

        # Iterate matrix
            # If reach land
                # Run BFS on cell
                    # Mark cells visited
                    # Count # of cells visited
                # Update max island area
        max_island_area = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] is LAND:
                    max_island_area = max(max_island_area, bfs(x, y))

        # return max island area
        return max_island_area