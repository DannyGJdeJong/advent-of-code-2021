def get_neighbours(dumbos, point):
    x, y = point

    x_max = len(dumbos) - 1
    y_max = len(dumbos[0]) - 1

    res = set()

    if x > 0:
        res.add((x - 1, y))

    if x > 0 and y > 0:
        res.add((x - 1, y - 1))

    if x > 0 and y < y_max:
        res.add((x - 1, y + 1))

    if y > 0:
        res.add((x, y - 1))

    if y < y_max:
        res.add((x, y + 1))

    if x < x_max:
        res.add((x + 1, y))

    if x < x_max and y > 0:
        res.add((x + 1, y - 1))

    if x < x_max and y < y_max:
        res.add((x + 1, y + 1))

    return res

dumbos = []

with open("input.txt") as f:
    for l in f:
        dumbos.append(list(map(int, l.strip())))

flash_count = 0

for _ in range(100):
    to_check = set()
    flashed = set()

    def check_flash(point):
        x, y = point

        global flash_count

        if dumbos[x][y] > 9 and point not in flashed:
            flashed.add(point)
            flash_count += 1
            neighbours = get_neighbours(dumbos, (x, y))
            for neighbour in neighbours:
                x_n, y_x = neighbour
                dumbos[x_n][y_x] += 1
                check_flash(neighbour)

    # Increase all by one
    for x in range(len(dumbos)):
        for y in range(len(dumbos[x])):
            dumbos[x][y] += 1

    # Flash!
    for x in range(len(dumbos)):
        for y in range(len(dumbos[x])):
            check_flash((x, y))

    for dumbo in flashed:
        x, y = dumbo
        dumbos[x][y] = 0

print(flash_count)

#==================#
# --- Part Two --- #
#==================#

dumbos = []

with open("input.txt") as f:
    for l in f:
        dumbos.append(list(map(int, l.strip())))

i = 0

while True:
    i += 1
    to_check = set()
    flashed = set()

    def check_flash(point):
        x, y = point

        global flash_count

        if dumbos[x][y] > 9 and point not in flashed:
            flashed.add(point)
            flash_count += 1
            neighbours = get_neighbours(dumbos, (x, y))
            for neighbour in neighbours:
                x_n, y_x = neighbour
                dumbos[x_n][y_x] += 1
                check_flash(neighbour)

    # Increase all by one
    for x in range(len(dumbos)):
        for y in range(len(dumbos[x])):
            dumbos[x][y] += 1

    # Flash!
    for x in range(len(dumbos)):
        for y in range(len(dumbos[x])):
            check_flash((x, y))

    for dumbo in flashed:
        x, y = dumbo
        dumbos[x][y] = 0

    if len(flashed) == len(dumbos) * len(dumbos[0]):
        print(i)
        break
