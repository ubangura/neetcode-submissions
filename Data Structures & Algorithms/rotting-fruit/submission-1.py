from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        FRESH = 1
        ROTTEN = 2
        # Iterate over matrix O(n x m)
            # collect rotten cell(s) in queue
            # count # of fresh fruit
        
        queue = deque()
        num_fresh_fruit = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                fruit = grid[row][col]

                if fruit is FRESH:
                    num_fresh_fruit += 1
                if fruit is ROTTEN:
                    queue.append((row, col))
        
        # Run BFS on queue O(n x m)
            # Each pop
                # Add adjacent fresh cells to queue
                    # Decrement count of fresh fruit
                    # Change cell value to 2 (rotten)
            # Each iteration of while loop (BFS), increment time
        time = 0
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and num_fresh_fruit:
            time += 1
            length = len(queue)

            for i in range(length):
                x, y = queue.popleft()

                for dx, dy in DIRECTIONS:
                    new_x, new_y = x + dx, y + dy

                    # Check cell is valid and fresh
                    if (0 <= new_x < len(grid)
                    and 0 <= new_y < len(grid[0])
                    and grid[new_x][new_y] == FRESH):
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = ROTTEN
                        num_fresh_fruit -= 1

        # return time if # of fresh fruit is 0, else -1
        return time if num_fresh_fruit == 0 else -1