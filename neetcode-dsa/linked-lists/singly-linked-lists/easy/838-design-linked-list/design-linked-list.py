# doubly linked list with hashmap
# pylint: disable=too-few-public-methods, invalid-name
# pylint: disable=missing-module-docstring missing-class-docstring, missing-function-docstring, missing-method-docstring


class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, self.tail, None)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = self.head
        for _ in range(index):
            node = node.next
        new_node = Node(val, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node
        self.size += 1

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        node = self.head
        for _ in range(index):
            node = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.size -= 1


# Example usage
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1, 2)
print(obj.get(1))  # Output: 2
obj.deleteAtIndex(1)
print(obj.get(1))  # Output: 3