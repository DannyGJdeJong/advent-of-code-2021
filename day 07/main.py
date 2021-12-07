def cost_of_position(positions, pos):
    return sum([abs(position - pos) for position in positions])

positions = []

with open("input.txt") as f:
    for l in f:
        nums = map(int, l.split(','))

        for num in nums:
            positions.append(num)

best_pos = sorted(positions)[len(positions) // 2]

print(f"Best position: {best_pos}")
print(f"Cost best position: {cost_of_position(positions, best_pos)}")

#==================#
# --- Part Two --- #
#==================#

def cost_of_position2(positions, pos):
    return sum([(abs(position - pos) * (abs(position - pos) + 1)) // 2 for position in positions])

best_pos = round(sum(positions) / len(positions))
best_cost = cost_of_position2(positions, best_pos)

cost_minus_one = cost_of_position2(positions, best_pos - 1)
cost_plus_one = cost_of_position2(positions, best_pos + 1)

if cost_minus_one < best_cost:
    best_pos = best_pos - 1

if cost_plus_one < best_cost:
    best_pos = best_pos + 1

print(f"Best position: {best_pos}")
print(f"Cost best position: {cost_of_position2(positions, best_pos)}")
