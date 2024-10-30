"""Program code"""

# David Barnes
# CIS 226
# 6-4-2023

# First-party imports
from droids import DroidCollection, Droid
from userinterface import UserInterface


def main(*args):
    """Method to run program"""

    # Create a new instance of droid collection
    droid_collection = DroidCollection()

    # NOTE: If you want to add hardcoded droids for testing, uncomment the following line:
    # add_hardcoded_droids(droid_collection)

    # Create a new instance of the user interface
    user_interface = UserInterface(droid_collection)

    # Display greeting to user
    user_interface.display_greeting()

    # Display main menu and get choice from user
    choice = user_interface.get_menu_choice(5, user_interface.display_main_menu)

    # While the choice is not 5 (exit)
    while choice < 5:
        # If 1, create droid
        if choice == 1:
            user_interface.create_droid()
        # sort category
        if choice == 2:
            user_interface.category_sort()

        # sort by total cost
        if choice == 3:
            user_interface.total_cost_sort()

        # print droid list
        elif choice == 4:
            user_interface.print_droid_list()
        # Re-prompt for input
        choice = user_interface.get_menu_choice(5, user_interface.display_main_menu)

    # Display exiting program message.
    user_interface.display_exit_message()


def add_hardcoded_droids(collection: DroidCollection) -> None:
    """method to add hardcoded droids"""
    collection.add_protocol(Droid.Materials.CARBONITE, Droid.Colors.WHITE, 1)
    collection.add_utility(Droid.Materials.VANADIUM, Droid.Colors.RED, True, True, True)
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
