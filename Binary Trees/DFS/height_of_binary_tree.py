class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

if __name__ == "__main__":

    tree = BinaryTree()

   
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)

    print("Inorder Traversal:")
    tree.inorder(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)

    print("\nHeight of Tree:")
    print(tree.height(tree.root))
