from .linked_list import LinkedList
from .key_value import KeyValue


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = LinkedList()
        self._set_sized_linked_list()

    def __str__(self):
        text = ''
        for i, node in enumerate(self.hash_table):
            text += f'{{<{i}>{str(node)}}}, '
        text = f'[{text[:-2]}]'
        return text

    def _set_sized_linked_list(self):
        for _ in range(self.size):
            self.hash_table.append(LinkedList())

    def _get_index_by_key(self, key):
        return hash(key) % self.size

    @staticmethod
    def _get_node_in_cell_by_key(cell, key):
        current = cell.head
        while current:
            if current.data.key == key:
                return current
            else:
                current = current.next
        return None

    def _get_cell_by_key(self, key):
        index = self._get_index_by_key(key)
        return self.hash_table[index].data

    def insert(self, key, value):
        cell = self._get_cell_by_key(key)
        node = self._get_node_in_cell_by_key(cell, key)
        if node is None:
            cell.append(KeyValue(key, value))
        else:
            node.data.value = value

    def lookup(self, key):
        cell = self._get_cell_by_key(key)
        node = self._get_node_in_cell_by_key(cell, key)
        if node:
            return node.data.value
        else:
            return None

    def delete(self, key):
        cell = self._get_cell_by_key(key)
        node = self._get_node_in_cell_by_key(cell, key)
        if node is not None:
            cell.delete(key)
