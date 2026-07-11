class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        WATER, LAND = 0, 1
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # DFS
        def dfs(x, y) -> int:
            if (0 <= x < ROWS
            and 0 <= y < COLS
            and grid[x][y] is LAND):
                grid[x][y] = WATER

                count = 0
                for dx, dy in DIRECTIONS:
                    count += dfs(x + dx, y + dy)
                
                return count + 1
            
            return 0

        # Iterate matrix
            # If reach land
                # Run DFS on cell
                    # Mark cells visited
                    # Count # of cells visited
                # Update max island area
        max_island_area = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] is LAND:
                    max_island_area = max(max_island_area, dfs(x, y))

        # return max island area
        return max_island_area