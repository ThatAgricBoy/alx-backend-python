#!/usr/bin/env python3
from typing import List

"""
a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
All elements of the list should be type-annotated as floats.
Args: input_list: list of floats
Return: sum of all elements of input_list

"""


def sum_list(input_list: List[float]) -> float:
    """ Args:
        input_list: list of floats
    Return:
        sum of all elements of input_list
    """
    return sum(input_list)
