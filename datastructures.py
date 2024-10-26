"""datastructures module"""

# System Imports
from abc import ABC
from typing import Any

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

    def _add_to_front(self, data) -> None:
        """method to add element to front of LL"""
        old_head = self._head
        self._head = self.Node()
        self._head.data = data
        self._head.next = old_head
        self._size += 1
        if self._size == 1:
            self._tail = self._head

    def _add_to_back(self, data) -> None:
        """add element to back of LL"""
        old_tail = self._tail
        self._tail = self.Node()
        self._tail.data = data
        self._size += 1
        if self._size == 1:
            self._head = self._tail
        else:
            old_tail.next = self._tail

    def _remove_from_front(self) -> Any:
        """remove element from front of LL"""
        if self.is_empty:
            raise IndexError("Nothing to remove.  List is Empty.")
        data = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self._size == 0:
            self._tail = None
        return data

    def _remove_from_back(self) -> Any:
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

    def get_data_at_index(self, index) -> Any:
        """method to index into LL"""
        if self.is_empty:
            raise IndexError("Nothing in list.")
        current_node = self._head
        counter: int = 0
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node.data

    @property
    def length(self) -> int:
        """length property"""
        return self.__calculate_length()

    def __calculate_length(self) -> int:
        """method to calculate length"""
        count: int = 0
        current_node = self._head
        if self.is_empty:
            return count
        if self._head == self._tail:
            count += 1
            return count
        while current_node != self._tail:
            count += 1
            current_node = current_node.next
        # add one more to count for tail
        count += 1
        return count


class Stack(AbstractLinkedList):
    """Stack Class"""

    def on_stack(self, data) -> None:
        """method to add to stack"""
        self._add_to_back(data)

    def off_stack(self) -> Any:
        """method to remove from stack"""
        return self._remove_from_back()


class Queue(AbstractLinkedList):
    """Queue Class"""

    def enqueue(self, data) -> None:
        """method to enqueue to back"""
        self._add_to_back(data)

    def dequeue(self) -> Any:
        """method to dequeue from front"""
        return self._remove_from_front()
