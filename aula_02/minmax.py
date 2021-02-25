from math import inf
from numbers import Number
from typing import Iterable, Tuple, Iterator


def _minmax_recursiva(iterador: Iterator, valor_minimo: Number, valor_maximo: Number):
    try:
        elemento = next(iterador)
    except StopIteration:
        return valor_minimo, valor_maximo
    else:
        if elemento < valor_minimo:
            valor_minimo = elemento
        if elemento > valor_maximo:
            valor_maximo = elemento
        return _minmax_recursiva(iterador, valor_minimo, valor_maximo)


def minmax(iteravel: Iterable) -> Tuple[Number, Number]:
    """
    >>> minmax([])
    Traceback (most recent call last):
        ...
    ValueError: não existe mínimo e máximo de iterável sem elemento
    >>> minmax([1])
    (1, 1)
    >>> minmax(range(900))
    (0, 899)
    >>> minmax(i for i in range(5))
    (0, 4)


    :param iteravel:
    :return:
    """
    iterador = iter(iteravel)
    valor_minimo, valor_maximo = _minmax_recursiva(iterador, inf, -inf)
    if valor_minimo is inf:
        raise ValueError('não existe mínimo e máximo de iterável sem elemento')
    return valor_minimo, valor_maximo
