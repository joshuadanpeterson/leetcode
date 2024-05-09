class Node:
    __slots__ = ["val", "next", "prev"]

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        mid_point = self.size // 2
        if index <= mid_point:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - 1, index, -1):
                node = node.prev
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val, None, self.tail)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
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
        for _ in range(index - 1):
            node = node.next
        new_node = Node(val, node.next, node)
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        if index == self.size:  # Updating the tail if needed
            self.tail = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
            self.size -= 1
            return
        if index == self.size - 1:
            if self.tail:
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None
            self.size -= 1
            return

        node = self.head
        for _ in range(index):
            node = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.size -= 1


# This ensures the list maintains integrity across various operations and corrects node linking/unlinking.

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index, val)
# obj.deleteAtIndex(index)

# obj.deleteAtIndex(index)