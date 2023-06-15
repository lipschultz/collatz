import math
from collections import Counter
from typing import Any, Dict, Generator, List, Mapping, Optional, Tuple

# import matplotlib.pyplot as plt


def collatz_sequence(starting_num: int) -> Generator[int, None, None]:
    yield starting_num

    num = starting_num
    while num != 1:
        num = (num // 2) if num % 2 == 0 else (3 * num + 1)
        yield num


def get_longest(sequences: List[List[int]]) -> Tuple[int, List[int]]:
    longest = max(sequences, key=lambda s: len(s))
    return longest[0], longest


def get_number_frequencies(sequences: List[List[int]]) -> Dict[int, int]:
    frequencies = Counter()
    for seq in sequences:
        frequencies.update(seq)
    return frequencies


def get_first_occurrences(sequences: List[List[int]]) -> Dict[int, int]:
    occurrences = {}
    for seq in reversed(sequences):
        n = seq[0]
        for val in seq:
            occurrences[val] = n
    return occurrences


def highest_values(sequences: List[List[int]]) -> Dict[int, int]:
    return {s[0]: max(s) for s in sequences}


def first_digit_frequency(sequences: List[List[int]]) -> Dict[int, int]:
    counter = Counter()
    for seq in sequences:
        counter.update(int(str(n)[0]) for n in seq)
    return {n: counter.get(n, 0) for n in range(min(counter), max(counter)+1)}


def fill_dict_gaps(number_map: Mapping[int, Any], gap_value: Any = 0, last_number: Optional[int] = None) -> Dict[int, Any]:
    complete_values = {}
    last_number = last_number or max(number_map)
    for n in range(1, last_number + 1):
        complete_values[n] = number_map.get(n, gap_value)
    return complete_values


def plot_benford(digit_frequencies: Mapping[int, int]):
    base = 10
    benford = [math.log(1 + 1/n, base) for n in range(1, base)]

    total = sum(digit_frequencies.values())
    plt.bar(digit_frequencies.keys(), digit_frequencies.values())

    plt.plot(digit_frequencies.keys(), [b * total for b in benford], color='orange')
