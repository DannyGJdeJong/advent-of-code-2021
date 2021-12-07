fish_ages = []

with open("input.txt") as f:
    for l in f:
        nums = l.split(',')

        for num in nums:
            fish_ages.append(int(num))

for _ in range(80):
    new_fish = []

    for i, fish in enumerate(fish_ages):
        if fish == 0:
            new_fish.append(8)
            fish_ages[i] = 6
        else:
            fish_ages[i] -= 1

    for fish in new_fish:
        fish_ages.append(fish)

print(len(fish_ages))

#==================#
# --- Part Two --- #
#==================#

fish_counts = [0] * 9

with open("input.txt") as f:
    for l in f:
        nums = l.split(',')

        for num in nums:
            fish_counts[int(num)] += 1

for i in range(256):
    new_fish_counts = [0] * 9

    for i, count in enumerate(fish_counts):
        if i == 0:
            new_fish_counts[8] += count
            new_fish_counts[6] += count
        else:
            new_fish_counts[i - 1] += count

    fish_counts = new_fish_counts

print(sum(fish_counts))
