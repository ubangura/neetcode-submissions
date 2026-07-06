from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_fresh_fruit = 0
        queue = deque()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                value = grid[x][y]

                if value == 1:
                    num_fresh_fruit += 1
                if value == 2:
                    queue.append((x,y))

        time = 0
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and num_fresh_fruit:
            time += 1

            for i in range(len(queue)):
                x, y = queue.popleft()
                
                for delta_x, delta_y in deltas:
                    dx, dy = x + delta_x, y + delta_y

                    if (dx < 0 or dx == len(grid)
                    or dy < 0 or dy == len(grid[0])
                    or grid[dx][dy] != 1):
                        continue
                
                    num_fresh_fruit -= 1
                    grid[dx][dy] = 2
                    queue.append((dx, dy))
                
        return time if num_fresh_fruit == 0 else -1
        