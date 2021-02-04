# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        def delete(node, parent, res):
            if not node: return None
            
            if node.val in to_delete:
                delete(node.left, None, res)
                delete(node.right, None, res)
                return None
            else:
                if not parent:
                    res.append(node)
                node.left = delete(node.left, node, res)
                node.right = delete(node.right, node, res)
                return node
        to_delete = set(to_delete)
        res = []
        delete(root, None, res)
        return res
                
                
                
                
                
                
                
                
        
