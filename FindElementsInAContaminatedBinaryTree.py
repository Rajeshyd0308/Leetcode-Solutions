# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements(object):

    # def bfs(self, target):
    #     ls= []
    #     ls.append(self.root_)
    #     while (len(ls)>0):
    #         u = ls.pop(0)
    #         if u!=None:
    #             if u.val==target:
    #                 return True
    #             else:
    #                 ls.append(u.left)
    #                 ls.append(u.right)
    #     return False
            
            
            
    def create_tree(self, t, val):
        
        if t.left!= None:
            t.left.val = 2*val+1
            self.set.add(2*val+1)
            self.create_tree(t.left, 2*val+1)

        if t.right!= None:
            t.right.val = 2*val+2
            self.set.add(2*val+2)
            self.create_tree(t.right, 2*val+2)
                
        
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        # self.last_elm = None
        # self.root_ = root
        self.set = set()
        if root!=None:
            root.val = 0
            self.create_tree(root, root.val)
        
        # return root
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        # print(self.last_elm)
        if len(self.set)==0:
            return False
        return target in self.set
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
