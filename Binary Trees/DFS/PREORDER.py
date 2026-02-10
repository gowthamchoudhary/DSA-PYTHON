class Node:
    def __init__(self,root):
        self.root = root
        self.right = None
        self.left = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode=Node(4)
fourthNode = Node(5)


firstNode.right = thirdNode
firstNode.left = secondNode
secondNode.left = fourthNode
def PreOrderSearch(node):
    if node is None:
        return
    print(node.root,end=",")
    PreOrderSearch(node.left)
    PreOrderSearch(node.right)
obj = PreOrderSearch(firstNode)


