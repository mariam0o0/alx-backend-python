#!/usr/bin/env python3
"""Annotate the function’s parameters and return values with the appropriate types"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotate function parameters"""
    return [(i, len(i)) for i in lst]
