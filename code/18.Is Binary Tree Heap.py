'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Your Function Should return True/False
    def isHeap(self, root):
        queue = [root]
        flag = False
        while queue:
            node = queue.pop(0)
            if node == None:
                flag = True
            elif flag:
                return False
            else:
                if node.left != None and node.data < node.left.data:
                    return False
                if node.right != None and node.data < node.right.data:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
