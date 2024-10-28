"""module to test mergesort"""
#Walter Podewil
#CIS 226
#October 28, 2024

#System Imports
from unittest import TestCase
#First Party Imports
from mergesort import MergeSort
#Third Party Imports

class PublicMerge(MergeSort):
        """class to expose protected methods"""
        def __init__(self):
            #create aux list at predefined length
            self._aux = [None for i in range(8)]
        def merge(self, mergeable, low, mid, high):
            """public merge method"""
            self._merge(mergeable, low, mid, high)

class TestPublicMerge(TestCase):
    """class to test PublicMerge, which exposes mergesort protected methods"""
    def setUp(self):
        """setup method"""
        self.my_merger = PublicMerge()
        self.sorted_thing_one = [1, 2, 3, 88]
        self.unsorted_thing_one = [3, 88, 2, 1]
        self.sorted_thing_two = [4, 66, 77, 99]
        self.unsorted_thing_two = [99, 77, 4, 66]
        self.merged_things = [1, 2, 3, 4, 66, 77, 88, 99]
        self.unmerged_things = [1, 2, 3, 88, 4, 66, 77, 99]

    def test_merge(self):
        """test merge method"""
        #Arrange


        low = 0
        mid = 3
        high = 7

        #Act
        self.my_merger.merge(self.unmerged_things, low, mid, high)

        #Assert
        self.assertEqual(self.unmerged_things, self.merged_things)

