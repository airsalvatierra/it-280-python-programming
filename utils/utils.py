from typing import List

def sort_low(integer_numbers: List) -> List:
    """
    sort a list of integer numbers in ascending order, and return sorted list
    """
    integer_numbers.sort()

def sort_high(integer_numbers: List) -> List:
    """
    sort a list of integer numbers in descending order, and return sorted list
    """
    integer_numbers.sort(reverse=True)

def remove_dup(integer_numbers: List) -> List:
    """
    remove duplicated itemos from a list of integers and return filtered list
    """
    return list(set(integer_numbers))
