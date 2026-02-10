class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
firstnode = Node(8)
secondnode = Node(3)
thirdnode = Node(10)
fourthnode = Node(1)
fifthnode = Node(6)
sixthnode = Node(4)
seventhnode = Node(7)


firstnode.left = secondnode
firstnode.right = thirdnode
secondnode.left = fourthnode
secondnode.right = fifthnode
fifthnode.left=sixthnode
fifthnode.right = seventhnode

def InorderTraversal(node):
    if node is None:
        return
    InorderTraversal(node.left)
    print(node.data,end="-->")
    InorderTraversal(node.right)

InorderTraversal(firstnode)