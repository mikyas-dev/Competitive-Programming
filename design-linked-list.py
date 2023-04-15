class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


class MyLinkedList:

    def __init__(self):
        self.head = Node(0) 
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:  
            return
        prev = self.head
        for i in range(index):
            prev = prev.next
        newNode = Node(val, prev.next)
        prev.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: 
            return
        prev = self.head
        for i in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1