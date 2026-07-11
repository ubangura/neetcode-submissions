"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # Create a list of 100 elements (default Node)
        nodes = [Node(i + 1, []) for i in range(100)]

        # BFS on start node
            # For each neighbor
                # If not visited
                    # Add to visited set
                    # Add to queue
                # Add the node at index neighbor.val - 1 to the adj. list for node at index curr.val - 1
        queue = deque([node])
        visited = {node}

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                
                nodes[node.val - 1].neighbors.append(nodes[neighbor.val - 1])

        # return node w/ val 1
        return nodes[0]