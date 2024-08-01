#!/usr/bin/env python3
"""typed-annotated function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Typed-annotated function"""
    return sum(mxd_lst)
