#!/usr/bin/env python3
"""type-annotated function sum_list, takes input_list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Typed-annotated function"""
    return sum(input_list)
