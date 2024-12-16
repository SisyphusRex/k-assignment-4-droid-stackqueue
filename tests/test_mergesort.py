"""module to test mergesort"""



# System Imports
from unittest import TestCase

# First Party Imports
from mergesort import MergeSort

# Third Party Imports


class TestMergeSort(TestCase):
    """Unprotected method class"""

    def setUp(self):
        """set up method"""
        self.my_merger = MergeSort()
        self.my_unsorted_mergeable: list[int] = [3, 8, 2, 5, 6]
        self.my_sorted_mergeable: list[int] = [2, 3, 5, 6, 8]

    def test_sort(self):
        """method to test main sort method"""
        # Arrange

        # Act
        self.my_merger.sort(self.my_unsorted_mergeable)

        # Asert
        self.assertEqual(self.my_sorted_mergeable, self.my_unsorted_mergeable)


class ProtectedMadePublic(MergeSort):
    """class to expose protected methods"""

    def __init__(self):
        # create aux list at predefined length
        self._aux = [None for i in range(10)]

    def merge_made_public(self, mergeable, low, mid, high):
        """make protected merge method public"""
        self._merge(mergeable, low, mid, high)

    def sort_made_public(self, mergeable, low, high):
        """make protected sort method public"""
        self._sort(mergeable, low, high)


class TestProtectedMethods(TestCase):
    """class to test PublicMerge, which exposes mergesort protected methods"""

    def setUp(self):
        """setup method"""
        self.my_merger = ProtectedMadePublic()
        self.merged_things = [1, 2, 3, 4, 5, 66, 77, 88, 99, 100]
        self.unmerged_things = [1, 2, 3, 5, 88, 4, 66, 77, 99, 100]
        self.unsorted_things = [75, 63, 80, 15, 4, 58, 99, 1, 100, 34]
        self.sorted_things = [1, 4, 15, 34, 58, 63, 75, 80, 99, 100]

    def test_sort_made_public(self):
        """test sort method"""
        # Arrange

        low = 0
        high = 9

        # Act
        self.my_merger.sort_made_public(self.unsorted_things, low, high)

        # Assert
        self.assertEqual(self.sorted_things, self.unsorted_things)

    def test_merge_made_public(self):
        """test merge method"""
        # Arrange
        low = 0
        mid = 4
        high = 9

        # Act
        self.my_merger.merge_made_public(self.unmerged_things, low, mid, high)

        # Assert
        self.assertEqual(self.merged_things, self.unmerged_things)
