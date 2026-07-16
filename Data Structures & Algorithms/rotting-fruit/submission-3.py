from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        num_fresh_fruit = 0
        queue = deque()

        for x in range(ROWS):
            for y in range(COLS):
                if grid[x][y] == FRESH:
                    num_fresh_fruit += 1
                if grid[x][y] == ROTTEN:
                    queue.append((x, y))

        time = 0

        while queue and num_fresh_fruit:
            time += 1

            level = len(queue)
            for cell in range(level):
                x, y = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy

                    if (0 <= new_x < ROWS
                    and 0 <= new_y < COLS
                    and grid[new_x][new_y] == FRESH):
                        grid[new_x][new_y] = ROTTEN
                        queue.append((new_x, new_y))
                        num_fresh_fruit -= 1

        return time if num_fresh_fruit == 0 else -1