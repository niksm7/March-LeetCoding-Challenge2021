'''Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None: # If the root node is empty return an empty list
            return []
        
        queue = [root] # This list will maintain the current level elements

        next_queue = [] # this list will maintain the child level elements i.e. the ones which are on one level below

        avg = [] # Averages of the levels will be stored here

        level_sum = 0
        
        while queue: # Run this loop until the queue list is empty

            for node in queue: # For each element of the current level

                level_sum += node.val # Add the value to the current level_sum

                if node.left: # if there is a child to the left

                    next_queue.append(node.left) # Append the child to the next_queue so that it can be accessed when the calculations for the next level are done

                if node.right:# if there is a child to the right

                    next_queue.append(node.right) # Append the child to the next_queue so that it can be accessed when the calculations for the next level are done
                
            avg.append(level_sum/len(queue)) # Calculate the average

            queue = next_queue # Move down one level by alloting the next_queue to be the current queue

            level_sum = 0 # re-initialize the level_sum to be 0

            next_queue = [] # As the child nodes are now the current nodes so this list becomes empty
            
        return avg # Return the average list