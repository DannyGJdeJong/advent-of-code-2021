import math

def is_low_point(grid, point):
    x, y = point

    x_gr_0 = x > 0
    x_lt_n = x < len(grid) - 1
    y_gr_0 = y > 0
    y_lt_n = y < len(grid[0]) - 1

    num = grid[x][y]

    if x_gr_0 and grid[x - 1][y] <= num:
        return 0

    if x_lt_n and grid[x + 1][y] <= num:
        return 0

    if y_gr_0 and grid[x][y - 1] <= num:
        return 0

    if y_lt_n and grid[x][y + 1] <= num:
        return 0

    return num + 1

grid = []

with open("input.txt") as f:
    for l in f:
        grid.append(list(map(int, l.strip())))

results = []

for x in range(len(grid)):
    for y in range(len(grid[0])):
        results.append(is_low_point(grid, (x, y)))

print(sum(results))

#==================#
# --- Part Two --- #
#==================#

def explore_point(grid, point):
    x, y = point
    num = grid[x][y]

    if num == 9:
        return set()

    x_gr_0 = x > 0
    x_lt_n = x < len(grid) - 1
    y_gr_0 = y > 0
    y_lt_n = y < len(grid[0]) - 1

    points = set()
    points.add((x, y))

    if x_gr_0 and grid[x - 1][y] > num:
        points |= explore_point(grid, (x - 1, y))

    if x_lt_n and grid[x + 1][y] > num:
        points |= explore_point(grid, (x + 1, y))

    if y_gr_0 and grid[x][y - 1] > num:
        points |= explore_point(grid, (x, y - 1))

    if y_lt_n and grid[x][y + 1] > num:
        points |= explore_point(grid, (x, y + 1))

    return points

basins = []

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if is_low_point(grid, (x, y)):
            points = set()
            points |= explore_point(grid, (x, y))
            basins.append(points)

basin_sizes = list(map(len, basins))

top_3 = sorted(basin_sizes, reverse=True)[:3]

print(f"{' * '.join(map(str, top_3))} = {math.prod(top_3)}")
