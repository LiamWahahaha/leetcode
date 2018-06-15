# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None:
            if root.left != None or root.right != None:
                tmp = root.right
                root.right = root.left
                root.left = tmp

            if root.left != None:
                self.invertTree(root.left)

            if root.right != None:
                self.invertTree(root.right)

        return root
