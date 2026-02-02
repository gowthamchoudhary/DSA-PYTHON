class SinglyNode:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)
Head.next = A
A.next = B  
B.next = C
print(Head) 


current = Head
while current:
    print(current.value)
    current = current.next