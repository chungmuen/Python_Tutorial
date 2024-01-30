"""
Module to store utility functions for test purposes.
"""
from os import path, mkdir
# importing os vs. importing os.path has no impact in python, but can add impact in other languages

VAR = 'slkjfdl'
def two_sum(nums, target):
    """ Find the index of the two first numbers that add up to target.

    :param nums: a list of numbers
    :param target: the value to reach
    :return: a list of the index of the two numbers
    :raises TypeError: if the target is not a number
    """
    print_statement('statement')
    if isinstance(target, str):
        raise TypeError("The target should be a number.")
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


def print_statement(statement):
    """ prints a statement

    :param statement: a string
    :return: a string
    """
    print(statement)
    return '123'


def create_download_directory():
    """ Creates a download directory if it doesn't exist

    :return: True or False
    """

    here = path.dirname(__file__)
    download_dir_path = path.join(here, 'downloads')
    # depending on the os, we might have different system for path, ex: "/", "\". using path.join, takes care of this

    if not path.exists(download_dir_path):
        mkdir(download_dir_path)
        return True
    return False


#if __name__ == "__main__":
#    create_download_directory()
# AVOID HAVING MAIN in a library!

