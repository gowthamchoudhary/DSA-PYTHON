#i hope i dont get stuck in linked lists again like last time

class SinglyNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
D = SinglyNode(5)

Head.next = A
A.next = B
B.next = C
C.next = D

print("Middle element is:", find_middle(Head))
