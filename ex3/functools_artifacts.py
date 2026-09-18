from typing import Callable, Any
from operator import add as oper_add, mul as oper_mul
from operator import max as oper_max, min as oper_min
from functools import reduce as funct_reduce
from functools import partial as funct_partial
from functools import lru_cache as funct_lru_cache
from functools import singledispatch as funct_singledispatch


spell_powers = [40, 20, 33, 37, 32, 24]
allowed_operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [13, 12, 15]

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in allowed_operations:
        print(f"Unknown operation: {operation}")
        return 0
    if operation == 'add':
        return funct_reduce(lambda x, y: oper_add(x, y), spells)
    if operation == 'multiply':
        return funct_reduce(lambda x, y: oper_mul(x, y), spells)
    if operation == 'max':
        return funct_reduce(lambda x, y: x if x > y else y, spells)
    if operation == 'min':
        return funct_reduce(lambda x, y: x if x < y else y, spells)


def test_spell_reducer() -> None:
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, "add")}")
    print(f"Product: {spell_reducer(spell_powers, "multiply")}")
    print(f"Max: {spell_reducer(spell_powers, "max")}")
    print()

def base_enchantment_funct(
    power: int, element: str, target:str
) -> str:pass
"""
partial_enchanter(base_enchantment) - Create partial applications:
• Take a base enchantment function with signature (power: int, element: str, target:
str) -> str
• Use functools.partial to create 3 specialized versions
• Each version pre-filling power=50 and the element
"""
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


def test_partial_enchanter() -> None:
    print("Testing partial enchanter ...")
    partial_enchanter()
    print()


"""
memoized_fibonacci(n) - Cached fibonacci:
• Use functools.lru_cache decorator for memoization
• Implement fibonacci sequence calculation
• Function should return the nth Fibonacci number
• The cache should improve performance for repeated calls
• Return the nth fibonacci number
INFO: You can verify caching works via memoized_fibonacci.cache_info().
"""
def memoized_fibonacci(n: int) -> int:
    pass

"""
spell_dispatcher() - Create single dispatch system:
• Use decorator functools.singledispatch to create a spell system
• The base function receives Any and handles unknown spell type
• Handle different types: int (damage spell), str (enchantment), list (multi-cast)
• Return the dispatcher function
• Each type should have appropriate spell behavior
"""
def spell_dispatcher() -> Callable[[Any], str]:
    pass


def test_memoized_fibonacci() -> None:
    print("Testing memoized fibonacci ...")
    memoized_fibonacci()
    print()


def test_spell_dispatcher() -> None:
    print("Testing spell dispatcher ...")
    spell_dispatcher()
    print()


def main() -> None:
    test_spell_reducer()
    test_partial_enchanter()
    test_memoized_fibonacci()
    test_spell_dispatcher()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
