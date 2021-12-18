from math import floor, ceil
from functools import reduce
import re

def explode(pair):
    pair = str(pair)
    depth = 0
    i_start = 0
    i_stop = 0

    for i, c in enumerate(pair):
        match c:
            case '[':
                depth += 1
            case ']':
                depth -= 1

        if depth > 4:
            i_start = i
            i_stop = pair[i:].find(']') + i_start + 1
            break

    if i_start == i_stop:
        return eval(pair)

    l, r = eval(pair[i_start:i_stop])

    numbers_match = re.compile(r"\b\d+\b")

    first_half = pair[:i_start]
    second_half = pair[i_stop:]

    last_l = None
    for num in numbers_match.finditer(first_half):
        last_l = num

    if last_l is not None:
        span_l, span_r = last_l.span()
        num = int(last_l.group()) + l
        first_half = first_half[:span_l] + str(num) + first_half[span_r:]

    first_r = None
    for num in numbers_match.finditer(second_half):
        first_r = num
        break

    if first_r is not None:
        span_l, span_r = first_r.span()
        num = int(first_r.group()) + r
        second_half = second_half[:span_l] + str(num) + second_half[span_r:]

    pair = first_half + "0" + second_half

    return eval(pair)

def reduce_split(pair):
    pair = str(pair)

    numbers_match = re.compile(r"\b\d+\b")
    first = None
    for num in numbers_match.finditer(pair):
        if int(num.group()) >= 10:
            first = num
            break

    if first is not None:
        span_l, span_r = first.span()
        num = int(first.group())
        pair = pair[:span_l] + str([floor(num / 2), ceil(num / 2)]) + pair[span_r:]

    return eval(pair)

def reduce_pair(pair):
    prev_res = []
    res = pair[:]

    while res != prev_res:
        prev_res = res

        res = explode(prev_res)

        if res == prev_res:
            res = reduce_split(prev_res)

    return res

snailfish_numbers = []

with open("input.txt") as f:
    for l in f:
        l = eval(l)
        snailfish_numbers.append(l)

solution = reduce(lambda l, r: reduce_pair([l, r]), snailfish_numbers)

def magnitude(pair):
    l, r = pair

    if type(l) != int:
        l = magnitude(l)

    if type(r) != int:
        r = magnitude(r)

    return 3 * l + 2 * r

print(magnitude(solution))

#==================#
# --- Part Two --- #
#==================#

max_magnitude = 0

for x, nums1 in enumerate(snailfish_numbers):
    for y, nums2 in enumerate(snailfish_numbers):
        if x == y:
            continue

        max_magnitude = max(max_magnitude, magnitude(reduce_pair([nums1, nums2])))

print(max_magnitude)
