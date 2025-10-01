# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def helper(node):
            if not node:
                return 0
            
            if (node) in memo:
                return memo[node]

            # take 
            take = node.val
            if node.left:
                take += helper(node.left.left) + helper(node.left.right)
            if node.right:
                take += helper(node.right.left) + helper(node.right.right)

            # not take
            not_take = helper(node.right) + helper(node.left)
            memo[node] = max(take, not_take)
            return memo[node]
        return helper(root)


            
