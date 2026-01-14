def linked_list():
    def __init__(self,value,prev=None):
        self.value=value
        self.next=None
    
    def finding_target(self,head,target):
        current = head
        while current:
             if current.value==target:
                return True
             else:
                 current=current.next
        return False



Head = linked_list(1)
A = linked_list(2)  
B = linked_list(3)
C = linked_list(4)
D = linked_list(5)
Head.next = A
A.next = B
B.next = C
C.next = D
print(linked_list.finding_target(Head,4))  

        