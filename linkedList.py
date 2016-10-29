class Node:
    def __init__(self, arg):
        self.data = data
        self.next = None

class Solution(object):
    def Display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self,head,data):
        node=Node(data)
        if head == None:
            node.next=None
            head=node
        else:
            current=head
            while current.next:
                current=current.next
            current.next=node
        return head

myList = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
myList.Display(head)
