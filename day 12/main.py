from collections import defaultdict

adjacencies = defaultdict(list)
large_caves = set()
small_caves = set()

with open("input.txt") as f:
    for l in f:
        v1, v2 = l.strip().split('-')

        if v1.isupper():
            large_caves.add(v1)

        if v2.isupper():
            large_caves.add(v2)

        adjacencies[v1].append(v2)
        adjacencies[v2].append(v1)

paths = []

def dfs(start, end, path):
    path.append(start)

    if start == end:
        paths.append(path.copy())
        return
    else:
        for adjacent in adjacencies[start]:
            if adjacent in large_caves or adjacent not in path:
                dfs(adjacent, end, path.copy())

    path.pop()

dfs("start", "end", [])
print(len(paths))

#==================#
# --- Part Two --- #
#==================#

adjacencies = defaultdict(list)
large_caves = set()
small_caves = set()

with open("input.txt") as f:
    for l in f:
        v1, v2 = l.strip().split('-')

        if v1.isupper():
            large_caves.add(v1)

        if v2.isupper():
            large_caves.add(v2)

        if v1.islower():
            small_caves.add(v1)

        if v2.islower():
            small_caves.add(v2)

        adjacencies[v1].append(v2)
        adjacencies[v2].append(v1)

small_caves.remove("start")
small_caves.remove("end")

paths = []

def dfs(start, end, path):
    path.append(start)

    if start == end:
        paths.append(path.copy())
        return
    else:
        for adjacent in adjacencies[start]:
            if adjacent in large_caves or (adjacent in small_caves and not any(path.count(e) > 1 for e in path if e in small_caves)) or adjacent not in path:
                dfs(adjacent, end, path.copy())

    path.pop()

dfs("start", "end", [])
print(len(paths))
