def pdi_function(number, base: int = 10):
    """Perfect digital invariant function."""
    total = 0
    while number > 0:
        total += pow(number % base, 2)
        number = number // base
    return total


def is_happy(number: int) -> bool:
    """Determine if the specified number is a happy number."""
    seen_numbers = set()
    while number > 1 and number not in seen_numbers:
        seen_numbers.add(number)
        number = pdi_function(number)
    return number == 1


def happy_path(number: int) -> list:
    seen_numbers = list()
    while number > 1 and number not in seen_numbers:
        seen_numbers.append(number)
        number = pdi_function(number)
    return seen_numbers
