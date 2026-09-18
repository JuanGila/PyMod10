from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    count = 0
    def increment_mage_counter():
        nonlocal count
        count += 1
        return count
    return lambda: increment_mage_counter()


def test_mage_counter() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    acumulated_power: int = initial_power
    def acumulate_power(power: int):
        nonlocal acumulated_power
        acumulated_power += power
        return acumulated_power
    return lambda power_amount: acumulate_power(power_amount)


def test_spell_accumulator() -> None:
    print("Testing spell accumulator...")
    spell_accumulator_a = spell_accumulator(100)
    print(f"Base 100, add 20: {spell_accumulator_a(20)}")
    print(f"Base 100, add 30: {spell_accumulator_a(30)}")
    print()


"""
enchantment_factory(enchantment_type) - Create enchantment functions:
• Return a function that applies the specified enchantment
• The returned function takes an item name and returns enchanted description
• Format: "enchantment_type item_name" (e.g., "Flaming Sword")
• Each factory creates functions with different enchantment types

Flaming Sword
Frozen Shield
"""
def enchantment_factory(enchantment_type: str) -> Callable:
    pass


def test_enchantment_factory() -> None:
    print("Testing enchantment factory...")
    enchantment_factory()
    print()


def memory_vault() -> dict[str, Callable[..., str | Any]]:
    stored_values: dict[str, Any] = {}
    
    def store(key: str, value: Any) -> None:
        stored_values[key] = value

    def recall(key: str) -> str | Any:
        if not stored_values.get(key):
            return "Memory not found"
        return stored_values[key]
    return {
        "store": lambda key, value: store(key, value),
        "recall": lambda key: recall(key)
    }


def test_memory_vault() -> None:
    print("Testing memory vault...")
    mem_vault = memory_vault()
    print("Store 'secret'= 42")
    mem_vault["store"]("secret", 42)
    print(f"Recall 'secret': {mem_vault["recall"]("secret")}")
    print(f"Recall 'unknown': {mem_vault["recall"]("unknown")}")
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
