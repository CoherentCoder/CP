class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        nonfullnodefound = False
        while queue:
            node = queue.pop(0)
            if node is None:
                nonfullnodefound = True
            elif nonfullnodefound:
                return False
            else:
                queue.append(node.left)
                queue.append(node.right)
        return True
