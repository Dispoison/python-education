import pytest

from ..linked_list import LinkedList
from ..queue import Queue
from ..stack import Stack
from ..hash_table import HashTable
from ..binary_search_tree import BinarySearchTree
from ..graph import Graph


class TestLinkedList:
    @staticmethod
    @pytest.fixture(name='linked_list')
    def linked_list_object():
        return LinkedList()

    @staticmethod
    @pytest.fixture(name='linked_list_filled')
    def linked_list_filled_object(linked_list):
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        return linked_list

    @staticmethod
    def test_prepend(linked_list):
        linked_list.prepend(2)
        assert linked_list.head.data == linked_list.tail.data == 2

    @staticmethod
    def test_append(linked_list):
        linked_list.append(2)
        assert linked_list.head.data == linked_list.tail.data == 2

    @staticmethod
    def test_append_prepend(linked_list):
        linked_list.append(2)
        linked_list.prepend(1)
        assert linked_list.head.data == 1 and linked_list.tail.data == 2

    @staticmethod
    def test_prepend_append(linked_list):
        linked_list.prepend(1)
        linked_list.append(2)
        assert linked_list.head.data == 1 and linked_list.tail.data == 2

    @staticmethod
    def test_prepend_prepend(linked_list):
        linked_list.prepend(2)
        linked_list.prepend(1)
        assert linked_list.head.data == 1 and linked_list.tail.data == 2

    @staticmethod
    def test_append_append(linked_list):
        linked_list.append(1)
        linked_list.append(2)
        assert linked_list.head.data == 1 and linked_list.tail.data == 2

    @staticmethod
    def test_append_prepend_append(linked_list):
        linked_list.append(2)
        linked_list.prepend(1)
        linked_list.append(3)
        assert linked_list.head.data == 1 and linked_list.tail.data == 3

    @staticmethod
    def test_prepend_append_prepend(linked_list):
        linked_list.prepend(2)
        linked_list.append(3)
        linked_list.prepend(1)
        assert linked_list.head.data == 1 and linked_list.tail.data == 3

    @staticmethod
    @pytest.mark.parametrize('data, expected', [(1, 0),
                                                (2, 1),
                                                (3, 2),
                                                (4, None)])
    def test_lookup(linked_list_filled, data, expected):
        assert linked_list_filled.lookup(data) == expected

    @staticmethod
    @pytest.mark.parametrize('index, data', [(0, 0),
                                             (1, 1.5),
                                             (2, 2.5)])
    def test_insert(linked_list_filled, index, data):
        old = linked_list_filled[index]
        linked_list_filled.insert(index, data)
        assert linked_list_filled[index].next == old

    @staticmethod
    @pytest.mark.parametrize('index, data', [(3, 4),
                                             (4, 5),
                                             (1000000000, 7)])
    def test_insert_over_length(linked_list_filled, index, data):
        linked_list_filled.insert(index, data)
        assert linked_list_filled[3].data == data

    @staticmethod
    def test_str_method(linked_list_filled):
        assert str(linked_list_filled) == '1, 2, 3'

    @staticmethod
    def test_len(linked_list):
        assert len(linked_list) == 0

    @staticmethod
    def test_len_one_node(linked_list):
        linked_list.append(0)
        assert len(linked_list) == 1

    @staticmethod
    def test_len_filled(linked_list_filled):
        assert len(linked_list_filled) == 3


class TestQueue:
    @staticmethod
    @pytest.fixture(name='queue')
    def queue_object():
        return Queue()

    @staticmethod
    @pytest.fixture(name='queue_filled')
    def queue_filled_object(queue):
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        return queue

    @staticmethod
    def test_enqueue(queue):
        queue.enqueue(1)
        queue.enqueue(3)
        queue.enqueue(2)
        assert str(queue) == '1, 3, 2'

    @staticmethod
    def test_dequeue(queue_filled):
        queue_filled.dequeue()
        queue_filled.dequeue()
        assert str(queue_filled) == '3'

    @staticmethod
    def test_peek(queue_filled):
        assert queue_filled.peek().data == 1 and str(queue_filled) == '1, 2, 3'


class TestStack:
    @staticmethod
    @pytest.fixture(name='stack')
    def stack_object():
        return Stack()

    @staticmethod
    @pytest.fixture(name='stack_filled')
    def stack_filled_object(stack):
        stack.push(1)
        stack.push(2)
        stack.push(3)
        return stack

    @staticmethod
    def test_push(stack):
        stack.push(3)
        stack.push(2)
        stack.push(1)
        assert str(stack) == '1, 2, 3'

    @staticmethod
    def test_pop(stack_filled):
        assert stack_filled.pop().data == 3 and str(stack_filled) == '2, 1'

    @staticmethod
    def test_peek(stack_filled):
        assert stack_filled.peek().data == 3 and str(stack_filled) == '3, 2, 1'


class TestHashTable:
    @staticmethod
    @pytest.fixture(name='hash_table')
    def hash_table_object():
        return HashTable(5)

    @staticmethod
    @pytest.fixture(name='hash_table_filled')
    def hash_table_filled_object(hash_table):
        hash_table.insert(0, 45)
        hash_table.insert(1, 54)
        hash_table.insert(2, '14')
        hash_table.insert(4, 5)
        hash_table.insert(6, 32)
        hash_table.insert(15, 212)
        hash_table.insert(20, 321)
        return hash_table

    @staticmethod
    def test_insert(hash_table):
        hash_table.insert(0, 1)
        hash_table.insert(5, 1)
        hash_table.insert(10, 1)
        hash_table.insert(15, 1)
        hash_table.insert(20, 1)
        hash_table.insert(8, 3)
        assert str(hash_table) == '[{<0>0: 1, 5: 1, 10: 1, 15: 1, 20: 1}, {<1>}, {<2>}, {<3>8: 3}, {<4>}]'

    @staticmethod
    @pytest.mark.parametrize('key, expected', [(0, 45),
                                               (20, 321),
                                               (6, 32),
                                               (4, 5),
                                               (1234567, None)])
    def test_lookup(hash_table_filled, key, expected):
        assert hash_table_filled.lookup(key) == expected

    @staticmethod
    @pytest.mark.parametrize('key, expected_str', [(1234567, '[{<0>0: 45, 15: 212, 20: 321}, {<1>1: 54, 6: 32}, '
                                                             '{<2>2: \'14\'}, {<3>}, {<4>4: 5}]'),
                                                   (0, '[{<0>15: 212, 20: 321}, {<1>1: 54, 6: 32}, '
                                                       '{<2>2: \'14\'}, {<3>}, {<4>4: 5}]'),
                                                   (20, '[{<0>0: 45, 15: 212}, {<1>1: 54, 6: 32}, '
                                                        '{<2>2: \'14\'}, {<3>}, {<4>4: 5}]'),
                                                   (6, '[{<0>0: 45, 15: 212, 20: 321}, {<1>1: 54}, '
                                                       '{<2>2: \'14\'}, {<3>}, {<4>4: 5}]'),
                                                   (1, '[{<0>0: 45, 15: 212, 20: 321}, {<1>6: 32}, '
                                                       '{<2>2: \'14\'}, {<3>}, {<4>4: 5}]')])
    def test_delete(hash_table_filled, key, expected_str):
        hash_table_filled.delete(key)
        assert str(hash_table_filled) == expected_str


class TestBinarySearchTree:
    @staticmethod
    @pytest.fixture(name='bst')
    def bst_object():
        return BinarySearchTree()

    @staticmethod
    @pytest.fixture(name='bst_filled')
    def bst_filled_object(bst):
        bst.insert(8)
        bst.insert(4)
        bst.insert(12)
        bst.insert(2)
        bst.insert(6)
        bst.insert(10)
        bst.insert(14)
        bst.insert(1)
        bst.insert(3)
        bst.insert(5)
        bst.insert(7)
        bst.insert(9)
        bst.insert(11)
        bst.insert(13)
        bst.insert(15)
        return bst

    @staticmethod
    def test_insert(bst):
        bst.insert(4)
        bst.insert(2)
        bst.insert(6)
        bst.insert(1)
        bst.insert(3)
        bst.insert(5)
        bst.insert(7)
        assert str(bst) == f'\t\t7\n' \
                           f'\t6\n' \
                           f'\t\t5\n' \
                           f'4\n' \
                           f'\t\t3\n' \
                           f'\t2\n' \
                           f'\t\t1\n'

    @staticmethod
    def test_lookup(bst_filled):
        assert bst_filled.lookup(4) == bst_filled.root.left

    @staticmethod
    def test_delete(bst_filled):
        bst_filled.delete(11)
        assert str(bst_filled) == f'\t\t\t15\n' \
                                  f'\t\t14\n' \
                                  f'\t\t\t13\n' \
                                  f'\t12\n' \
                                  f'\t\t10\n' \
                                  f'\t\t\t9\n' \
                                  f'8\n' \
                                  f'\t\t\t7\n' \
                                  f'\t\t6\n' \
                                  f'\t\t\t5\n' \
                                  f'\t4\n' \
                                  f'\t\t\t3\n' \
                                  f'\t\t2\n' \
                                  f'\t\t\t1\n'


class TestGraph:
    @staticmethod
    @pytest.fixture(name='graph')
    def graph_object():
        return Graph()

    @staticmethod
    @pytest.fixture(name='graph_filled')
    def graph_filled_object(graph):
        graph.insert('A')
        a = graph.lookup('A')
        graph.insert('B', a)
        b = graph.lookup('B')
        graph.insert('C', b)
        graph.insert('D', a)
        return graph

    @staticmethod
    def test_insert(graph_filled):
        assert str(graph_filled) == "A - ['B', 'D'], B - ['A', 'C'], C - ['B'], D - ['A']"

    @staticmethod
    def test_lookup(graph_filled):
        b = graph_filled.lookup('B')
        links = b.data.value
        assert b.data.key == 'B' and links.head.data.data.key == 'A' and links.head.next.data.data.key == 'C'

    @staticmethod
    def test_delete(graph_filled):
        a = graph_filled.lookup('A')
        graph_filled.delete(a)
        assert str(graph_filled) == "B - ['C'], C - ['B'], D - []"
