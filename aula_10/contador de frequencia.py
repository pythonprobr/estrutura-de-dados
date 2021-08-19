"""
    >>> contar_frequencia('banana')
    {'b': 1, 'a': 3, 'n': 2}
"""
from collections import Counter
from typing import Iterable


def contar_frequencia(iteravel: Iterable):
    return dict(Counter(iteravel).items())
