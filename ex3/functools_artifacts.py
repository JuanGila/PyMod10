from typing import Callable, Any
from operator import add as oper_add, mul as oper_mul
from functools import (
    reduce as funct_reduce,
    partial as funct_partial,
    lru_cache as funct_lru_cache,
    singledispatch as funct_singledispatch
)


generated_fibonacci_tests = [13, 12, 15]
generated_spell_powers = [40, 20, 33, 37, 32, 24]
generated_allowed_spell_operations = ['add', 'multiply', 'max', 'min']


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in generated_allowed_spell_operations:
        raise ValueError(f"Unknown operation: {operation}")
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
    print(f"Sum: {spell_reducer(generated_spell_powers, "add")}")
    print(f"Product: {spell_reducer(generated_spell_powers, "multiply")}")
    print(f"Max: {spell_reducer(generated_spell_powers, "max")}")
    print()

def base_enchantment_funct(
    power: int, element: str, target:str
) -> str:
    return f"Power: {power}, Element: {element}, Target: {target}"
"""
partial_enchanter(base_enchantment) - Create partial applications:
• Take a base enchantment function with signature (power: int, element: str, target: str) -> str
• Use functools.partial to create 3 specialized versions
• Each version pre-filling power=50 and the element
"""
def partial_enchanter(
    base_enchantment: Callable[[int , str, str], str]
) -> dict[str, Callable]:
    return {
        "fire": lambda enchantment_target: funct_partial(
            base_enchantment,
            power=50, element="fireball",
            target=enchantment_target
        ),
        "ice": lambda enchantment_target: funct_partial(
            base_enchantment,
            power=50, element="ice",
            target=enchantment_target
        ),
        "shadow": lambda enchantment_target: funct_partial(
            base_enchantment,
            power=50, element="shadow",
            target=enchantment_target
        )
    }

def test_partial_enchanter() -> None:
    print("Testing partial enchanter ...")
    enchantment = partial_enchanter(
        base_enchantment_funct("¿base_enchantment_funct?")
    )
    print(enchantment["fire"])
    print(enchantment["ice"])
    print(enchantment["shadow"])
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


def test_memoized_fibonacci() -> None:
    print("Testing memoized fibonacci ...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()


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


def test_spell_dispatcher() -> None:
    print("Testing spell dispatcher ...")
    """
    Damage spell: 42 damage
    Enchantment: fireball
    Multi-cast: 3 spells
    Unknown spell type
    """
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
