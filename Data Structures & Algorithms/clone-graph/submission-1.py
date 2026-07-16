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
        
        # Create a map of old nodes to deep copy
        old_to_new = {}

        # BFS on start node
            # For each neighbor
                # If not visited
                    # Add to visited set
                    # Add to queue
                # Add the neighbor deep copy to the adj. list for the deep copy of the curr node
        queue = deque([node])
        visited = {node}
        old_to_new[node] = Node(node.val, [])

        while queue:
            old_node = queue.popleft()

            for neighbor in old_node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val, [])

                old_to_new[old_node].neighbors.append(old_to_new[neighbor])

        # return node w/ val 1
        return old_to_new[node]