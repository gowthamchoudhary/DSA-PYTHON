class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

first = Node(13)
second = Node(7)
third = Node(15)
fourth = Node(3)
fifth = Node(8)
sixth = Node(14)
seventh = Node(19)
eighth = Node(18)


first.left = second
first.right = third
second.left = fourth
second.right = fifth
third.left = sixth
third.right = seventh
seventh.left=eighth

def search(node, target):
  if node is None:
    return None
  elif node.data == target:
    return node
  elif target < node.data:
    return search(node.left, target)
  else:
    return search(node.right, target)


key = int(input("Enter an Integer"))
# Search for a value
result = search(first, key)
if result:
  print(f"Found the node with value: {result.data}")
else:
  print("Value not found in the BST.")

