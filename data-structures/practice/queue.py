from .linked_list import LinkedList


class Queue(LinkedList):
    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        if self.head is None:
            return None
        first = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return first

    def peek(self):
        return self.head
