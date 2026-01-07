class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        curr_head = self.head
        node.next = curr_head
        self.head = node
        return

        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index <= 0:
            self.addAtHead(val)
            return
        curr = self.head
        prev = None
        count = 0
        while curr:
            if count == index:
                prev.next = new_node
                new_node.next = curr
                return

            prev = curr 
            curr = curr.next  
            count += 1

        if count == index:
            prev.next = new_node
            self.tail = new_node


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or not self.head:
            return

        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return
        curr = self.head
        prev = None
        count = 0
        while curr:
            if count == index:
                prev.next = curr.next
                if curr == self.tail:
                    self.tail = prev
                return
            prev = curr
            curr = curr.next
            count += 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)