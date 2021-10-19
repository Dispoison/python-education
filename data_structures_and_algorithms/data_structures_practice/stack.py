from .linked_list import LinkedList


class Stack(LinkedList):
    def push(self, value):
        self.prepend(value)

    def pop(self):
        if self.head is None:
            return None
        first = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return first

    def peek(self):
        return self.head
