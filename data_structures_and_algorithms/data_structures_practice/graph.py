from .linked_list import LinkedList
from .key_value import KeyValue


class Graph:
    def __init__(self):
        self.nodes = LinkedList()

    def __str__(self):
        text = ''
        for node in self.nodes:
            if node.data.value:
                text += f'{str(node.data.key)} - '
                text += '['
                for link_node in node.data.value:
                    text += f'{repr(link_node.data.data.key)}, '
                text = text[:-2] + '], '
            else:
                text += f'{str(node.data.key)} - [], '
        text = f'{text[:-2]}'
        return text

    def _join_with_other_nodes(self, node_name, node_name_to_link):
        main = self.lookup(node_name)
        to_link = self.lookup(node_name_to_link)
        to_link.data.value.append(main)

    def insert(self, node_name, *nodes_to_link):
        links = LinkedList()
        self.nodes.append(KeyValue(node_name, links))
        for node in nodes_to_link:
            links.append(node)
            self._join_with_other_nodes(node_name, node.data.key)

    def lookup(self, node_name):
        return self.nodes[self.nodes.lookup(node_name)]

    def delete(self, node):
        for node_link in node.data.value:
            for link in node_link.data.data.value:
                if link.data.data.key == node.data.key:
                    node_link.data.data.value.delete(link.data)
        self.nodes.delete(node.data.key)
