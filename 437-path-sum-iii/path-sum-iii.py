# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        # Count paths starting from current node
        def dfs(node, currentSum):
            if not node:
                return 0
            count = 1 if node.val == currentSum else 0
            count += dfs(node.left, currentSum - node.val)
            count += dfs(node.right, currentSum - node.val)
            return count

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
