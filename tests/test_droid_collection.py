"""droid collection test module"""

# Walter Podewil
# CIS 226
# October 30, 2024

# System Imports
from unittest import TestCase

# First Party Imports
from droids import DroidCollection
from droids import Droid

# Third Party Imports


class TestDroidCollection(TestCase):
    """test droid collection class"""

    def setUp(self):
        self.my_collection = DroidCollection()
        self.add_hardcoded_droids(self.my_collection)
        self.sorted_by_category: list[str] = [
            "Astromech",
            "Astromech",
            "Janitor",
            "Janitor",
            "Utility",
            "Utility",
            "Protocol",
            "Protocol",
        ]
        self.sorted_by_cost: list[float] = [
            255.00,
            270.00,
            320.00,
            340.00,
            375.00,
            420.00,
            575.00,
            585.00,
        ]

    def add_hardcoded_droids(self, collection: DroidCollection) -> None:
        """method to add hardcoded droids"""
        collection.add_protocol(Droid.Materials.CARBONITE, Droid.Colors.WHITE, 1)
        collection.add_utility(
            Droid.Materials.VANADIUM, Droid.Colors.RED, True, True, True
        )
        collection.add_astromech(
            Droid.Materials.QUADRANIUM, Droid.Colors.GREEN, True, True, True, True, 1
        )
        collection.add_janitor(
            Droid.Materials.TEARS_OF_A_JEDI,
            Droid.Colors.BLUE,
            True,
            True,
            True,
            True,
            True,
        )
        collection.add_protocol(Droid.Materials.TEARS_OF_A_JEDI, Droid.Colors.BLUE, 2)
        collection.add_utility(
            Droid.Materials.QUADRANIUM, Droid.Colors.GREEN, False, False, False
        )
        collection.add_astromech(
            Droid.Materials.VANADIUM, Droid.Colors.RED, False, False, False, False, 0
        )
        collection.add_janitor(
            Droid.Materials.CARBONITE,
            Droid.Colors.WHITE,
            False,
            False,
            False,
            False,
            False,
        )

    def test_sort_by_category(self):
        """method to test sort by category"""
        # Arrange
        models: list[str] = []
        # Act
        self.my_collection.sort_by_category()
        for droid in self.my_collection._collection:
            models.append(droid.model_name)

        # Assert
        self.assertEqual(self.sorted_by_category, models)

    def test_sort_by_total_cost(self):
        """method to test sort by total cost"""
        # arrange
        total_costs: list[float] = []
        # Act
        self.my_collection.sort_by_total_cost()
        for droid in self.my_collection._collection:
            total_costs.append(droid.total_cost)

        # Assert
        self.assertEqual(self.sorted_by_cost, total_costs)
