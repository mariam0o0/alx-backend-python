#!/usr/bin/env python3
""" Annotate the function’s parameters and return values"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns elements of the list with its length"""
    return [(i, len(i)) for i in lst]
