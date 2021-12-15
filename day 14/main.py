import collections
from operator import add

template = ""
insertion_rules = dict()

with open("input.txt") as f:
    # Read template
    template = f.readline().strip()

    # Skip newline
    f.readline()

    # Read insertion rules
    for l in f:
        pair, letter = l.strip().split(' -> ')
        insertion_rules[pair] = letter

def get_pairs(polymer: str) -> list:
    return map(add, polymer[:-1], polymer[1:])

polymer = template

for _ in range(10):
    pairs = get_pairs(polymer)

    to_insert = []

    for pair in pairs:
        to_insert.append(insertion_rules[pair])

    polymer = ''.join(map(add, polymer[:-1], to_insert)) + polymer[-1]

most_common = max(set(polymer), key=polymer.count)
most_common_count = polymer.count(most_common)
least_common = min(set(polymer), key=polymer.count)
least_common_count = polymer.count(least_common)

print(f"Most common element: {most_common} ({most_common_count})")
print(f"Least common element: {least_common} ({least_common_count})")
print(f"{most_common_count} - {least_common_count} = {most_common_count - least_common_count}")

#==================#
# --- Part Two --- #
#==================#

from collections import Counter

step_count = 40
step_count += 1

unique_letters = set(''.join(map(lambda x: x[0], insertion_rules)))
letter_count_template = {x:0 for x in unique_letters}

def get_letter_counts(polymer: str):
    letter_counts = Counter()

    for letter in unique_letters:
        letter_counts[letter] = polymer.count(letter)

    return letter_counts

letter_counts_at_step = [dict() for _ in range(step_count)]

for pair, letter in insertion_rules.items():
    letter_counts_at_step[0][pair] = get_letter_counts(pair)

for i in range(1, step_count):
    for pair, letter in insertion_rules.items():
        letter_counts_at_step[i][pair] = letter_counts_at_step[i - 1][pair[0] + letter] + letter_counts_at_step[i - 1][letter + pair[1]] - Counter({letter: 1})

final_counter = sum([letter_counts_at_step[step_count - 1][pair] for pair in get_pairs(template)], collections.Counter())

# Adjust for double counted characters at the start
final_counter -= Counter(template[1:-1])

most_common, most_common_count = final_counter.most_common()[0]
least_common, least_common_count = final_counter.most_common()[-1]

print(f"Most common element: {most_common} ({most_common_count})")
print(f"Least common element: {least_common} ({least_common_count})")
print(f"{most_common_count} - {least_common_count} = {most_common_count - least_common_count}")
