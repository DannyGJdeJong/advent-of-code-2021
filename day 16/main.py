from math import prod

transmission = ""

with open("input.txt") as f:
    transmission = f.readline().strip()

transmission = ''.join([bin(int(c, 16))[2:].zfill(4) for c in transmission])

versions = []

def read(pointer):
    V = int(transmission[pointer:pointer+3], 2)
    T = int(transmission[pointer+3:pointer+6], 2)

    versions.append(V)

    pointer += 6

    value = ""

    match T:
        case 4:
            while True:
                group = transmission[pointer:pointer+5]
                value += group[1:]
                pointer += 5

                if group[0] == "0":
                    value = int(value, 2)
                    break

        case _:
            I = int(transmission[pointer], 2)

            pointer += 1
            values = []

            match I:
                case 0:
                    length_in_bits = int(transmission[pointer:pointer+15], 2)
                    pointer += 15

                    end = pointer + length_in_bits

                    while pointer < end:
                        temp_pointer, value = read(pointer)
                        pointer = temp_pointer
                        values.append(value)
                case 1:
                    length = int(transmission[pointer:pointer+11], 2)
                    pointer += 11

                    for _ in range(length):
                        temp_pointer, value = read(pointer)
                        pointer = temp_pointer
                        values.append(value)

            match T:
                case 0:
                    value = sum(values)
                case 1:
                    value = prod(values)
                case 2:
                    value = min(values)
                case 3:
                    value = max(values)
                case 5:
                    value = 1 if values[0] > values[1] else 0
                case 6:
                    value = 1 if values[0] < values[1] else 0
                case 7:
                    value = 1 if values[0] == values[1] else 0

    return pointer, value

val = read(0)

print(sum(versions))

#==================#
# --- Part Two --- #
#==================#

print(val)
