from queue import PriorityQueue

grid = []

with open("input.txt") as f:
    for l in f:
        grid.append(list(map(int, l.strip())))

adjancencies = dict()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        adjacent_coords = [(x, y) for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if x >= 0 and x < len(row) and y >= 0 and y < len(grid)]
        adjancencies[(x, y)] = []

        for coord in adjacent_coords:
            c_x, c_y = coord
            adjancencies[(x, y)].append((coord, grid[c_y][c_x]))

start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)

visited = set()

distances = {coord:float('inf') for coord in adjancencies.keys()}
distances[start] = 0

to_visit = PriorityQueue()
to_visit.put((0, start))

while not to_visit.empty():
    distance, current = to_visit.get()
    visited.add(current)

    for adjacent in adjancencies[current]:
        adj_coord, adj_distance = adjacent

        if adj_coord not in visited:
            old_distance = distances[adj_coord]
            new_distance = adj_distance + distance

            if new_distance < old_distance:
                to_visit.put((new_distance, adj_coord))
                distances[adj_coord] = new_distance

print(distances[end])

#==================#
# --- Part Two --- #
#==================#

new_grid = []

for i in range(5):
    for row in grid:
        base_row = [x + i if x + i < 10 else (x + i) % 10 + 1 for x in row]
        new_row = [cell for sublist in [[x + j if x + j < 10 else (x + j) % 10 + 1 for x in base_row] for j in range(5)] for cell in sublist]
        new_grid.append(new_row)

grid = new_grid

adjancencies = dict()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        adjacent_coords = [(x, y) for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if x >= 0 and x < len(row) and y >= 0 and y < len(grid)]
        adjancencies[(x, y)] = []

        for coord in adjacent_coords:
            c_x, c_y = coord
            adjancencies[(x, y)].append((coord, grid[c_y][c_x]))

start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)

visited = set()

distances = {coord:float('inf') for coord in adjancencies.keys()}
distances[start] = 0

to_visit = PriorityQueue()
to_visit.put((0, start))

while not to_visit.empty():
    distance, current = to_visit.get()
    visited.add(current)

    for adjacent in adjancencies[current]:
        adj_coord, adj_distance = adjacent

        if adj_coord not in visited:
            old_distance = distances[adj_coord]
            new_distance = adj_distance + distance

            if new_distance < old_distance:
                to_visit.put((new_distance, adj_coord))
                distances[adj_coord] = new_distance

print(distances[end])
