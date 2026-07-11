class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER, LAND = "0", "1"
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        # DFS
        def dfs(x, y) -> None:
            if (0 <= x < ROWS
            and 0 <= y < COLS
            and grid[x][y] == LAND):
                grid[x][y] = WATER
                for dx, dy in DIRECTIONS:
                    dfs(x + dx, y + dy)

        # Iterate over matrix
            # If reach land
                # Increment num_islands
                # Run DFS on cell
                    # Mark cells visited (change value to "0")
        num_islands = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == LAND:
                    num_islands += 1
                    dfs(x, y)

        # return num_islands
        return num_islands