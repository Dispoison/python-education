class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.root:
            self.root.tab = ''
        return str(self.root)

    def _insert_node(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data, node)
            else:
                self._insert_node(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data, node)
            else:
                self._insert_node(node.right, data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)

    def _lookup_node(self, node, data):
        if node is None:
            return None

        if data < node.data:
            return self._lookup_node(node.left, data)
        elif data > node.data:
            return self._lookup_node(node.right, data)
        else:
            return node

    def lookup(self, data):
        return self._lookup_node(self.root, data)

    def _get_most_left_node(self, node):
        if node.left is None:
            return node
        return self._get_most_left_node(node.left)

    def _get_most_right_node(self, node):
        if node.right is None:
            return node
        return self._get_most_right_node(node.right)

    def _on_replace(self, node, est_node_from):
        est_node_from.left = node.left
        est_node_from.right = node.right
        est_node_from.parent = node.parent
        if node.left:
            node.left.parent = est_node_from
        if node.right:
            node.right.parent = est_node_from

    def _update_parent(self, node, est_node_from):
        if node.parent is None:
            self.root = est_node_from
        else:
            if node.parent.left is node:
                node.parent.left = est_node_from
            if node.parent.right is node:
                node.parent.right = est_node_from

    def delete(self, data):
        node = self.lookup(data)
        if node.left is None and node.right is None:
            if node.parent:
                if node.parent.left is node:
                    node.parent.left = None
                elif node.parent.right is node:
                    node.parent.right = None
            else:
                self.root = None
        elif node.left:
            rightest_node_from_left = self._get_most_right_node(node.left)
            if node.left is rightest_node_from_left:
                if node.parent:
                    node.left.parent = node.parent
                else:
                    node.left.parent = None
                    rightest_node_from_left.right = node.right
                if node.right:
                    rightest_node_from_left.right = node.right
                    node.right.parent = rightest_node_from_left
            else:
                if rightest_node_from_left.left:
                    rightest_node_from_left.left.parent = rightest_node_from_left.parent
                    rightest_node_from_left.parent.right = rightest_node_from_left.left
                else:
                    rightest_node_from_left.parent.right = None
                self._on_replace(node, rightest_node_from_left)
            self._update_parent(node, rightest_node_from_left)
        elif node.right:
            leftest_node_from_right = self._get_most_left_node(node.right)
            if node.right is leftest_node_from_right:
                if node.parent:
                    node.right.parent = node.parent
                else:
                    node.right.parent = None
                    leftest_node_from_right.left = node.left
                if node.left:
                    leftest_node_from_right.left = node.left
                    node.left.parent = leftest_node_from_right
            else:
                if leftest_node_from_right.right:
                    leftest_node_from_right.right.parent = leftest_node_from_right.parent
                    leftest_node_from_right.parent.left = leftest_node_from_right.right
                else:
                    leftest_node_from_right.parent.left = None
                self._on_replace(node, leftest_node_from_right)
            self._update_parent(node, leftest_node_from_right)


class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.tab = ''

    def __str__(self):
        text = ''
        if self.right:
            self.right.tab = self.tab + '\t'
            text += str(self.right)

        text += f'{self.tab}{str(self.data)}\n'

        if self.left:
            self.left.tab = self.tab + '\t'
            text += str(self.left)
        return text
