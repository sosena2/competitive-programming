# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = 0
        def dfs(node, s):
            if node is None:
                return 0 

            s = s*10 + node.val

            # leaves
            if node.right is None and node.left is None:
                return s
                
            # recursivelly find the left and right sum
            left_sum = dfs(node.left, s)
            right_sum = dfs(node.right, s)

            return right_sum + left_sum
        return dfs(root, s)
