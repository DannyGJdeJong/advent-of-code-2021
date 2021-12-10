def flip_bracket(bracket):
    if bracket == ')':
        return '('

    if bracket == ']':
        return '['

    if bracket == '}':
        return '{'

    if bracket == '>':
        return '<'

    if bracket == '(':
        return ')'

    if bracket == '[':
        return ']'

    if bracket == '{':
        return '}'

    if bracket == '<':
        return '>'

lines = []

with open("input.txt") as f:
    for l in f:
        lines.append(l.strip())

illegals = []

for line in lines:
    chars = []

    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            chars.append(char)
        if char == ')' or char == ']' or char == '}' or char == '>':
            last_char = chars.pop()
            if last_char != flip_bracket(char):
                illegals.append(char)
                break

score = 0

for illegal in illegals:
    if illegal == ')':
        score += 3

    if illegal == ']':
        score += 57

    if illegal == '}':
        score += 1197

    if illegal == '>':
        score += 25137

print(score)

#==================#
# --- Part Two --- #
#==================#

def is_corrupted(line):
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            chars.append(char)
        if char == ')' or char == ']' or char == '}' or char == '>':
            last_char = chars.pop()
            if last_char != flip_bracket(char):
                return True

    return False

def get_score(chars):
    score = 0

    for char in chars:
        score *= 5

        if char == ')':
            score += 1

        if char == ']':
            score += 2

        if char == '}':
            score += 3

        if char == '>':
            score += 4

    return score

# Discard corrupted lines
lines = [line for line in lines if not is_corrupted(line)]

scores = []

for line in lines:
    chars = []

    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            chars.append(char)
        if char == ')' or char == ']' or char == '}' or char == '>':
            chars.pop()

    scores.append(reversed([flip_bracket(char) for char in chars]))

scores = [get_score(score) for score in scores]
print(sorted(scores)[len(scores) // 2])
