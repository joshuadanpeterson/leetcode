class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.val
            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        count = 0
        while current is not None:
            if count == index - 1:
                new_node = Node(val, current.next)
                current.next = new_node
                return
            count += 1
            current = current.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current is not None:
            if count == index - 1 and current.next is not None:
                current.next = current.next.next
                return
            count += 1
            current = current.next

# Example usage
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1)) # Should return 2
# obj.deleteAtIndex(1)
# print(obj.get(1)) # Should return 3