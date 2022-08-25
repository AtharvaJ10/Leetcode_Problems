# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize_helper(self, root):
        if root:
            self.encode.append(str(root.val))
            self.serialize_helper(root.left)
            self.serialize_helper(root.right)
        else:
            self.encode.append("#")
            

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.encode = []
        self.serialize_helper(root)
        res = ' '.join(self.encode)
        return res
        
    def deserialize_helper(self):
        if self.queue:
            node = self.queue.popleft()
            if node!="#":
                root = TreeNode(node)
                root.left = self.deserialize_helper()
                root.right = self.deserialize_helper()
                return root
            else:
                return None
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(" ")
        self.queue = deque([])
        for i in data:
            self.queue.append(i)
        return self.deserialize_helper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))