class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

firstNode = Node(2)
secondNode = Node(3)
thirdNode=Node(4)
fourthNode = Node(5)


firstNode.right = thirdNode
firstNode.left = secondNode
secondNode.left = fourthNode
def PreOrderTraversal(node):
    if node is None:
        return
    print(node.data,end=",")
    PreOrderTraversal(node.left)
    PreOrderTraversal(node.right)
obj = PreOrderTraversal(firstNode)


