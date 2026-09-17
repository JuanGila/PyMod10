from typing import Callable


""""
mage_counter() - Create a counting closure:
• Return a function that counts how many times it’s been called
• Each call should return the current count (starting from 1)
• The counter should persist between calls
• Creating two separate counters must yield independent state.
• Use closure to maintain state without global variables
"""
def mage_counter() -> Callable:
    return lambda x: x + 1


"""
spell_accumulator(initial_power) - Create power accumulator:
• Return a function that accumulates power over time
• Each call adds the given amount to the total power
• Return the new total power after each addition
• Start with initial_power as the base
"""
def spell_accumulator(initial_power: int) -> Callable:
    pass


"""
enchantment_factory(enchantment_type) - Create enchantment functions:
• Return a function that applies the specified enchantment
• The returned function takes an item name and returns enchanted description
• Format: "enchantment_type item_name" (e.g., "Flaming Sword")
• Each factory creates functions with different enchantment types
"""
def enchantment_factory(enchantment_type: str) -> Callable:
    pass


"""memory_vault() - Create a memory management system:
• Return a dict with ’store’ and ’recall’ functions
• ’store’ function: takes (key, value) and stores the memory
• ’recall’ function: takes (key) and returns stored value or "Memory not found"
• Use closure to maintain private memory storage
"""
def memory_vault() -> dict[str, Callable]:
    pass


def test_mage_counter() -> None:
    print("Testing mage counter...")
    mage_counter()
    print()


def test_spell_accumulator() -> None:
    print("Testing spell accumulator...")
    spell_accumulator()
    print()


def test_enchantment_factory() -> None:
    print("Testing enchantment factory...")
    enchantment_factory()
    print()


def test_memory_vault() -> None:
    print("Testing memory vault...")
    memory_vault()
    print()


def main() -> None:
    test_mage_counter()
    test_spell_accumulator()
    test_enchantment_factory()
    test_memory_vault()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting ...")
    except BaseException as base_err:
        print(f"\n{base_err.__class__.__name__}: {base_err}")
