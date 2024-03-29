   def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
        def __init__(self):
            self.same = True
        def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if(p is None and q is None):
            return True
        else:
            if(p is None or q is None or p.val != q.val):
                return False
            
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
