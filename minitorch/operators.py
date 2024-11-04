"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, Any

#
# Implementation of a prelude of elementary functions.

def mul(a: float, b: float) -> float:
    return a * b

def id(a) -> int:
    return a

def add(a: float, b: float) -> float:
    return a + b

def neg(a: float) -> float:
    return -1.0 * a

def lt(a: float, b: float) -> float:
    return 1.0 if a < b else 0.0

def eq(a: float, b: float) -> float:
    return 1.0 if a == b else 0.0

def max(a: float, b: float) -> float:
    return a if a > b else b

def is_close(a: float, b: float) -> float:
    return 1.0 if abs(a - b) < 1e-2 else 0.0

def sigmoid(a: float) -> float:
    return inv(1.0 + exp(neg(a))) if a >= 0 else exp(a) / (1.0 + exp(a))
   
def relu(a: float) -> float:
    return a if a > 0 else 0.0

def log(a: float) -> float:
    return math.log(a)

def exp(a: float) -> float:
    return math.exp(a)

def log_back(a: float, b: float) -> float:
    return inv(a) * b

def inv(a: float) -> float:
    return 1.0 / a

def inv_back(a: float, b: float) -> float:
    return neg(inv(a)**2) * b

def relu_back(a: float, b: float) -> float:
    return b if a > 0 else 0.0

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(func: Callable, iterable: Iterable[float]):
    for item in iterable:
        yield func(item)

def zipWith(iterable1: Iterable[float], iterable2: Iterable[float]):
    for item1, item2 in zip(iterable1, iterable2):
        yield (item1, item2)

def reduce(func: Callable, iterable: Iterable[float], init_val: Any) -> float:
    res = init_val
    for item in iterable:
        res = func(item, res)
    return res

def negList(a: Iterable[float]) -> Iterable[float]:
    return list(map(neg, a))

def addLists(a: Iterable[float], b: Iterable[float]) -> Iterable[float]:
    return list(map(lambda a: a[0] + a[1], zipWith(a, b)))

def prod(a: Iterable[float]) -> float:
    return reduce(mul, a, 1.0)

def sum(a: Iterable[float]) -> float:
    return reduce(add, a, 0.0)

# TODO: Implement for Task 0.3.
