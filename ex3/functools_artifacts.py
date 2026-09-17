from typing import Callable, Any


"""
spell_reducer(spells, operation) - Reduce spell powers:
• Use functools.reduce to combine all spell powers
• Support operations: "add", "multiply", "max", "min"
• Use operator module functions (add, mul, etc.)
• Return the final reduced value
• If spells is empty, return 0
• If operation is unknown, properly handle the error
"""
def spell_reducer(spells: list[int], operation: str) -> int:
    pass


"""
partial_enchanter(base_enchantment) - Create partial applications:
• Take a base enchantment function with signature (power: int, element: str, target:
str) -> str
• Use functools.partial to create 3 specialized versions
• Each version pre-filling power=50 and the element
"""
def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


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


def test_spell_reducer() -> None:
    print("Testing spell reducer...")
    spell_reducer()
    print()


def test_partial_enchanter() -> None:
    print("Testing partial enchanter...")
    partial_enchanter()
    print()


def test_memoized_fibonacci() -> None:
    print("Testing memoized fibonacci...")
    memoized_fibonacci()
    print()


def test_spell_dispatcher() -> None:
    print("Testing spell dispatcher...")
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
