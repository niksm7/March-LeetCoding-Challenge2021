'''Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        current_level = [root] # This will hold all the nodes of the current level as we move down into depth of the tree

        next_level = [] # This will hold the child nodes of all the current nodes

        count = 1 # We initialize count to be 1 because the root node has a depth of 1

        # Now if given depth to be filled with val is given as 1 that means this value will be the root and the complete tree will now be its child to the left

        if d == 1:
            x = TreeNode(val=v,left=root)
            return x

        # If depth is greater than 1 we go down until we reach the particular depth

        while count != d:

            for i in current_level: # Each time take nodes from current level and append their child to next level list

                if i.right:
                    next_level.append(i.right)
                if i.left:
                    next_level.append(i.left)

            count += 1 # We increase the count as we go down
            
            if count != d: # Only if the depth is still not met we will now go down to the next level else we won't as we will need the depth-1 pair of nodes

                current_level = next_level
                next_level = []
            
        for i in current_level: # Now the current level nodes need to have their next level filled with the val that is provided.

            # We first stored already existing left and right nodes in temporary variables
            temp1 = i.left
            temp2 = i.right

            # and then we add the new nodes with value provided and with their left and right nodes pointing to the left and right nodes stored in temp variables

            i.left = TreeNode(val=v,left=temp1,right=None)
            i.right = TreeNode(val=v,left=None,right=temp2)
            
        
        #Finally after making the changes we return the root node
        return root