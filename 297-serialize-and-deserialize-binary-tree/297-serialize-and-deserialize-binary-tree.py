# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize_helper(self, node):
        if not node:
            self.encode.append("#")
            return
        self.encode.append(str(node.val))
        self.serialize_helper(node.left)
        self.serialize_helper(node.right)
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.encode = []
        self.serialize_helper(root)
        return ' '.join(self.encode)
    
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
        self.queue = deque([])
        data = data.split(" ")
        for i in data:
            self.queue.append(i)
        return self.deserialize_helper()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))