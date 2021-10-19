class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __getitem__(self, key):
        if isinstance(key, int):
            current = self.head
            for _ in range(key):
                current = current.next
                if current is None:
                    raise IndexError
            return current
        else:
            raise TypeError

    def __iter__(self):
        return LinkedListIterator(self.head)

    def __len__(self):
        length = 0
        if self.head is None:
            return length
        current = self.head
        while current:
            current = current.next
            length += 1
        return length

    def __str__(self):
        text = ''
        for node in self:
            if self.head:
                text += f'{str(node.data)}, '
        text = f'{text[:-2]}'
        return text

    def prepend(self, data):
        if self.head is None:
            self.head = self.tail = LinkedListNode(data)
        else:
            self.head = LinkedListNode(data, self.head)

    def append(self, data):
        if self.tail is None:
            self.tail = self.head = LinkedListNode(data)
        else:
            tail = LinkedListNode(data)
            self.tail.next = tail
            self.tail = tail

    def lookup(self, data):
        counter = 0
        current = self.head
        while current:
            if current.data == data:
                return counter
            else:
                counter += 1
                current = current.next
        return None

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
        else:
            try:
                pre_target = self[index-1]
                pre_target.next = LinkedListNode(data, pre_target.next)
            except IndexError:
                self.append(data)

    def delete(self, data):
        index = self.lookup(data)
        if index is not None:
            if index == 0:
                if self.head is self.tail:
                    self.tail = None
                self.head = self.head.next
            else:
                pre_target = self[index-1]
                if pre_target.next is self.tail:
                    self.tail = pre_target
                pre_target.next = pre_target.next.next

    def _data(self):
        return (node.data for node in self)


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        return self.get_next()

    def __iter__(self):
        return self

    def get_next(self):
        if self.current is None:
            raise StopIteration
        result = self.current
        self.current = self.current.next
        return result


class LinkedListNode:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return str(self.data)
