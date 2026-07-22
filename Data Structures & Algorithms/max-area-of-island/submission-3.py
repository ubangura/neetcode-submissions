class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        WATER, LAND = 0, 1

        def dfs(x, y) -> int:
            if (0 <= x < ROWS
            and 0 <= y < COLS
            and grid[x][y] == LAND):
                grid[x][y] = WATER
                
                count = 0
                for dx, dy in DIRECTIONS:
                    count += dfs(x + dx, y + dy)
            
                return count + 1

            return 0

        max_area = 0

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == LAND:
                    max_area = max(max_area, dfs(x, y))

        return max_area