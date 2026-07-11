
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        WATER = "0"
        LAND = "1"
        DIRECTIONS = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        # DFS
        def dfs(grid, x, y) -> None:
            if (0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and grid[x][y] == LAND):
                grid[x][y] = WATER
                for dx, dy in DIRECTIONS:
                    dfs(grid, x + dx, y + dy)

        # Iterate over matrix
            # If reach land
                # Increment num_islands
                # Run DFS on cell
                    # Mark cells visited (change value to "0")
        num_islands = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == LAND:
                    num_islands += 1
                    dfs(grid, x, y)

        # return num_islands
        return num_islands