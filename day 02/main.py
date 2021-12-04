commands = []

with open("input.txt") as f:
    for l in f:
        l = l.strip()
        command, val = l.split(' ')
        commands.append((command, int(val)))

# Horizontal pos
x = 0
# Depth
y = 0

for command, val in commands:
    if command == "forward":
        x += val
    if command == "up":
        y -= val
    if command == "down":
        y += val

print(x * y)

#==================#
# --- Part Two --- #
#==================#

# Horizontal pos
x = 0
# Depth
y = 0
# Aim
z = 0

for command, val in commands:
    if command == "forward":
        x += val
        y += z * val
    if command == "up":
        z -= val
    if command == "down":
        z += val

print(x * y)
