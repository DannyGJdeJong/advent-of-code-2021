algorithm = ""
image = []

with open("input.txt") as f:
    # Read algorithm
    algorithm = f.readline().strip()

    # Skip newline
    f.readline()

    # Read image
    for l in f:
        image.append(l.strip())

# Add dots around the image
def expand(image, char):
    image = image[:]

    width = len(image[0])

    dots = char * width
    image.insert(0, dots)
    image.insert(0, dots)
    image.insert(0, dots)
    image.insert(0, dots)
    image.append(dots)
    image.append(dots)
    image.append(dots)
    image.append(dots)

    new_image = []

    for l in image:
        new_image.append(char * 4 + l + char * 4)

    return new_image

def trim(image, char):
    char = '#' if char == '.' else '.'

    new_image = image[2:-2]

    new_image = [row[2:-2] for row in new_image]

    return new_image


def pretty_print(image):
    for l in image:
        print(l)

def get_character(x, y, image):
    number = image[y - 1][x - 1:x + 2] + image[y][x - 1:x + 2] + image[y + 1][x - 1:x + 2]
    number = int(''.join(['0' if num == '.' else '1' for num in number]), 2)

    return algorithm[number]

def step(image, char):
    image = expand(image, char)

    new_image = [list(row) for row in image]

    for y, row in enumerate(image):
        if y == 0 or y == len(image) - 1:
            continue

        for x, c in enumerate(row):
            if x == 0 or x == len(row) - 1:
                continue
            new_image[y][x] = get_character(x, y, image)

    new_image = trim([''.join(row) for row in new_image], char)

    return new_image

after_two_steps = step(step(image, '.'), '#')

hashtag_count = 0

for row in after_two_steps:
    hashtag_count += row.count('#')

print(hashtag_count)

#==================#
# --- Part Two --- #
#==================#

char = '.'

result = image

for _ in range(50):
    result = step(result, char)

    char = '#' if char == '.' else '.'

hashtag_count = 0

for row in result:
    hashtag_count += row.count('#')

print(hashtag_count)
