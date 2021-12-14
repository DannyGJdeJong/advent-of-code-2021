coords = []
folds = []
parse_folds = False

with open("input.txt") as f:
    for l in f:
        if l == '\n':
            parse_folds = True
            continue

        if not parse_folds:
            x, y = l.split(',')
            x = int(x)
            y = int(y)

            coords.append((x, y))
        else:
            direction, num = l.split('=')
            direction = direction[-1]
            num = int(num)
            folds.append((direction, num))

max_x = max([x for x, _ in coords]) + 1
max_y = max([y for _, y in coords]) + 1

grid = [[False] * max_x for _ in range(max_y)]

for x, y in coords:
    grid[y][x] = True

first_fold = [folds[0]]

for direction, num in first_fold:
    match direction:
        case "x":
            new_grid = [[False] * num for _ in range(len(grid))]
            for y_i, row in enumerate(grid):
                for x_i, cell in enumerate(row):
                    if x_i < num :
                        new_grid[y_i][x_i] = cell
                    if cell and x_i > num:
                        new_x = num - (x_i - num)
                        new_grid[y_i][new_x] |= True
            grid = new_grid

        case "y":
            new_grid = [[False] * len(grid[0]) for _ in range(num)]
            for y_i, row in enumerate(grid):
                for x_i, cell in enumerate(row):
                    if y_i < num:
                        new_grid[y_i][x_i] = cell
                    if cell and y_i > num:
                        new_y = num - (y_i - num)
                        new_grid[new_y][x_i] |= True
            grid = new_grid

print(sum(map(sum, grid)))

#==================#
# --- Part Two --- #
#==================#

coords = []
folds = []
parse_folds = False

with open("input.txt") as f:
    for l in f:
        if l == '\n':
            parse_folds = True
            continue

        if not parse_folds:
            x, y = l.split(',')
            x = int(x)
            y = int(y)

            coords.append((x, y))
        else:
            direction, num = l.split('=')
            direction = direction[-1]
            num = int(num)
            folds.append((direction, num))

max_x = max([x for x, _ in coords]) + 1
max_y = max([y for _, y in coords]) + 1

grid = [[False] * max_x for _ in range(max_y)]

for x, y in coords:
    grid[y][x] = True

for direction, num in folds:
    match direction:
        case "x":
            new_grid = [[False] * num for _ in range(len(grid))]
            for y_i, row in enumerate(grid):
                for x_i, cell in enumerate(row):
                    if x_i < num :
                        new_grid[y_i][x_i] = cell
                    if cell and x_i > num:
                        new_x = num - (x_i - num)
                        new_grid[y_i][new_x] |= True
            grid = new_grid

        case "y":
            new_grid = [[False] * len(grid[0]) for _ in range(num)]
            for y_i, row in enumerate(grid):
                for x_i, cell in enumerate(row):
                    if y_i < num:
                        new_grid[y_i][x_i] = cell
                    if cell and y_i > num:
                        new_y = num - (y_i - num)
                        new_grid[new_y][x_i] |= True
            grid = new_grid

for row in grid:
    print(''.join(map(lambda x: '#' if x else '.', row)))
