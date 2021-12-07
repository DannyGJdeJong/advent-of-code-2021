def is_horizontal_or_vertical(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2

coords = [[0] * 1000 for _ in range(1000)]

with open("input.txt") as f:
    for l in f:
        c1, c2 = l.split('->')
        x1, y1 = c1.split(',')
        x2, y2 = c2.split(',')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if is_horizontal_or_vertical(x1, y1, x2, y2):
            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    coords[x1][y] += 1
            if y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    coords[x][y1] += 1

result = 0

for row in coords:
    for cell in row:
        if cell >= 2:
            result += 1

print(result)

#==================#
# --- Part Two --- #
#==================#

coords = [[0] * 1000 for _ in range(1000)]

with open("input.txt") as f:
    for l in f:
        c1, c2 = l.split('->')
        x1, y1 = c1.split(',')
        x2, y2 = c2.split(',')

        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                coords[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                coords[x][y1] += 1
        else:
            if y1 < y2:
                x = x1
                for y in range(y1, y2 + 1):
                    coords[x][y] += 1
                    if x1 > x2:
                        x -= 1
                    else:
                        x += 1
            else:
                x = x2
                for y in range(y2, y1 + 1):
                    coords[x][y] += 1
                    if x2 > x1:
                        x -= 1
                    else:
                        x += 1

result = 0

for row in coords:
    for cell in row:
        if cell >= 2:
            result += 1

print(result)
