"""datastructures module"""

# System Imports
from abc import ABC

# First Party Imports

# Third Party Imports


class AbstractLinkedList(ABC):
    """abstract linked list class"""

    class Node:
        """node in linked list"""

        def __init__(self):
            """constructor"""
            self.data = None
            self.next = None

    def __init__(self):
        """constructor"""
        self._size = 0
        self._head = None
        self._tail = None

    @property
    def is_empty(self) -> bool:
        """compares memory location of self._head"""
        return self._head is None

    def add_to_front(self, data) -> None:
        """method to add element to front of LL"""
        old_head = self._head
        self._head = self.Node()
        self._head.data = data
        self._head.next = old_head
        self._size += 1
        if self._size == 1:
            self._tail = self._head

    def add_to_back(self, data) -> None:
        """add element to back of LL"""
        old_tail = self._tail
        self._tail = self.Node()
        self._tail.data = data
        old_tail.next = self._tail
        self._size += 1
        if self._size == 1:
            self._head = self._tail
        else:
            old_tail.next = self._tail

    def remove_from_front(self) -> ...:
        """remove element from front of LL"""
        if self.is_empty:
            raise IndexError("Nothing to remove.  List is Empty.")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return data

    def remove_from_back(self) -> ...:
        """method to remove element from back of LL"""
        if self.is_empty:
            raise IndexError("Nothing to remove.  List is empty.")

        data = self._tail.data

        if self._head == self._tail:
            self._tail = None
            self._head = None
        else:
            current_node = self._head
            while current_node.next != self._tail:
                current_node = current_node.next
            self._tail = current_node
            self._tail.next = None
        self._size -= 1
        return data
