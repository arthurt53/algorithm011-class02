class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# 迭代
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)
        return res


#  递归
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left :
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
