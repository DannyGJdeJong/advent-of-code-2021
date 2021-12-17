x_min = 0
x_max = 0
y_min = 0
y_max = 0

with open("input.txt") as f:
    l = f.readline().strip()
    _, _, x, y = l.split()
    x = x[2:-1]
    y = y[2:]

    x_min, x_max = map(int, x.split(".."))
    y_min, y_max = map(int, y.split(".."))

highest_y = 0

def fire(x_i, y_i):
    x = 0
    y = 0
    v_x = x_i
    v_y = y_i

    largest_y = 0

    while True:
        x += v_x
        y += v_y
        v_x += -1 if v_x > 0 else (1 if v_x < 0 else 0)
        v_y -= 1

        largest_y = max(largest_y, y)

        if x >= x_min and x <= x_max and y >= y_min and y <= y_max:
            return largest_y

        if (x_i < 0 and x < x_min) or (x_i > 0 and x > x_max) or y < y_min:
            return float("-inf")

hits = 0

for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        height = fire(x, y)
        highest_y = max(height, highest_y)
        if height > -99999:
            hits += 1

print(highest_y)

#==================#
# --- Part Two --- #
#==================#

print(hits)
