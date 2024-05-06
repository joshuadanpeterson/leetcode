class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if not self.tail:  # If the list was empty, now head is also the tail
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node  # List was empty

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        for i in range(index - 1):
            if not current:
                return
            current = current.next
        if current:
            new_node = Node(val, current.next)
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.head:
                self.head = self.head.next
            if not self.head:
                self.tail = None
            return
        current = self.head
        for i in range(index - 1):
            if not current or not current.next:
                return
            current = current.next
        if current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next

# Example usage
# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1)) # Should return 2
# obj.deleteAtIndex(1)
# print(obj.get(1)) # Should return 3