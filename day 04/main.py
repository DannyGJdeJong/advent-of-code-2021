numbers_to_draw = []
bingo_cards = []
drawn_numbers = []

with open("input.txt") as f:
    l = f.readline()
    numbers_to_draw = [int(n) for n in l.split(',')]

    # Skip empty line
    l = f.readline()

    bingo_card = []

    for l in f:
        if l.strip() == '':
            bingo_cards.append(bingo_card)
            bingo_card = []
            continue

        nums = [int(n) for n in l.strip().replace('  ', ' ').split(' ')]
        bingo_card.append(nums)

def has_bingo(bingo_card):
    for row in bingo_card:
        if all([x in drawn_numbers for x in row]):
            return True
    for col in range(len(bingo_card)):
        if all([x in drawn_numbers for x in [row[col] for row in bingo_card]]):
            return True
    return False

def calc_score(bingo_card):
    score = 0

    for row in bingo_card:
        for num in row:
            if num not in drawn_numbers:
                score += num
    score *= drawn_numbers[-1]

    return score

for num in numbers_to_draw:
    drawn_numbers.append(num)
    bingos = [has_bingo(bingo_card) for bingo_card in bingo_cards]

    if any(bingos):
        i = bingos.index(True)
        print(calc_score(bingo_cards[i]))
        break

#==================#
# --- Part Two --- #
#==================#

last_index = -1

for num in numbers_to_draw:
    drawn_numbers.append(num)
    bingos = [not has_bingo(bingo_card) for bingo_card in bingo_cards]

    # If only one hasn't won
    if sum(bingos) == 1:
        last_index = bingos.index(True)
        continue

    if sum(bingos) == 0 and last_index >= 0:
        print(calc_score(bingo_cards[last_index]))
        break
