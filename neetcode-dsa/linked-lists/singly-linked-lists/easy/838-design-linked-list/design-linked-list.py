# doubly linked list
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
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
        new_node = Node(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        if self.tail:
            node = self.head
            for _ in range(index - 1):
                if node is None:
                    return
                node = node.next
            if node is self.tail:
                self.addAtTail(val)
            elif node and node.next:
                new_node = Node(val, node, node.next)
                node.next.prev = new_node
                node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        node = self.head
        for _ in range(index):
            if node is None:
                return
            node = node.next
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        elif node:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

# Example usage
# obj = MyDoublyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1))  # Should return 2
# obj.deleteAtIndex(1)
# print(obj.get(1))  # Should return 3