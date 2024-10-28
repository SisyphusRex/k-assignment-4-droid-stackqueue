"""data structures test module"""
#Walter Podewil
#CIS 226
#October 28, 2024

#System Imports
from unittest import TestCase
#First Party Imports
from datastructures import Stack, Queue
#Third Party Imports


class StackTest(TestCase):
    """class to test stack class"""

    def setUp(self):
        """setUp method"""
        self.thing = 11
        self.second_thing = 22
        self.my_stack = Stack()

    def test_is_empty_when_empty(self):
        """method to test is empty"""
        #Arrange

        #Act

        #Assert
        self.assertTrue(self.my_stack.is_empty)

    def test_is_empty_when_populated(self):
        """method to test is empty when not empty"""
        #Arrange
        self.my_stack.on_stack(self.thing)

        #Act

        #Assert
        self.assertFalse(self.my_stack.is_empty)

    def test_get_data_from_index(self):
        """test get data from index method"""
        #Arrange
        self.my_stack.on_stack(self.thing)
        self.my_stack.on_stack(self.second_thing)

        #Act
        things_data = self.my_stack.get_data_at_index(0)
        second_things_data = self.my_stack.get_data_at_index(1)

        #Assert
        self.assertEqual(things_data, self.thing)
        self.assertEqual(second_things_data, self.second_thing)

    def test_on_stack_to_empty_stack(self):
        """method to test on stack method adding one object to empty stack"""
        #Arrange

        #Act
        self.my_stack.on_stack(self.thing)

        #Assert
        self.assertEqual(self.my_stack.length, 1)

    def test_on_stack_to_populated_stack(self):
        """method to test on stack to populated stack"""
        #Arrange
        self.my_stack.on_stack(self.thing)

        #Act
        self.my_stack.on_stack(self.second_thing)

        #Assert
        self.assertEqual(self.my_stack.get_data_at_index(1), self.second_thing)

    def test_off_stack_one_object(self):
        """method to test off stack method with one object in stack"""
        #Arrange
        self.my_stack.on_stack(self.thing)
        #Act
        data = self.my_stack.off_stack()
        #Assert
        self.assertEqual(self.my_stack.length, 0)
        self.assertEqual(data, self.thing)

    def test_off_stack_populated_stack(self):
        """method to test if off stack removes from same side as on stack"""
        #Arrange
        self.my_stack.on_stack(self.thing)
        self.my_stack.on_stack(self.second_thing)

        #Act
        data = self.my_stack.off_stack()

        #Assert
        self.assertEqual(data, self.second_thing)

class QueueTest(TestCase):
    """class to test Queue"""
    def setUp(self):
        """set up method"""
        self.thing = 11
        self.second_thing = 22
        self.my_queue = Queue()

    def test_enqueue_to_empty_queue(self):
        """method to test enqueue of adding one object to empty queue"""
        #Arrange

        #Act
        self.my_queue.enqueue(self.thing)
        #Assert
        self.assertEqual(self.my_queue.length, 1)

    def test_enqueue_to_populated_queue(self):
        """method to test enqueue to populated queue, should add to back"""

        #Arrange
        self.my_queue.enqueue(self.thing)

        #Act
        self.my_queue.enqueue(self.second_thing)

        #Assert
        self.assertEqual(self.my_queue.get_data_at_index(1), self.second_thing)

    def test_dequeue_one_object(self):
        """method to test dequeu when one object in queue"""
        #Arrange
        self.my_queue.enqueue(self.thing)
        #Act
        data = self.my_queue.dequeue()
        #Assert
        self.assertEqual(self.my_queue.length, 0)
        self.assertEqual(data, self.thing)

    def test_dequeue_from_populated_queue(self):
        """method to test dequeue from populated queue, should remove from front"""
        #Arrange
        self.my_queue.enqueue(self.thing)
        self.my_queue.enqueue(self.second_thing)

        #Act
        data = self.my_queue.dequeue()

        #Assert
        self.assertEqual(data, self.thing)