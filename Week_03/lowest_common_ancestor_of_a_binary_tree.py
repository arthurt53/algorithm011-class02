class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursion terminator 递归终止条件
        if not root or root == p or root == q: return root
        # drill down  下探到下一层
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # process logic in current level 处理当前层逻辑
        if not left: return right
        if not right: return left
        return root
