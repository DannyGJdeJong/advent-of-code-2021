from abc import abstractproperty


outputs = []

with open("input.txt") as f:
    for l in f:
        output = l.split('|')[1].strip().split(' ')
        outputs.append([num.strip() for num in output])

count = 0

for output in outputs:
    for num in output:
        length = len(num)
        if length == 2 or length == 3 or length == 4 or length == 7:
            count += 1

print(count)

#==================#
# --- Part Two --- #
#==================#

inputs = []

with open("input.txt") as f:
    for l in f:
        input = l.split('|')[0].strip().split(' ')
        inputs.append([set(num.strip()) for num in input])

sum = 0

for i, input in enumerate(inputs):
    nums = [set() for _ in range(10)]
    nums[1] = [num for num in input if len(num) == 2][0]
    nums[4] = [num for num in input if len(num) == 4][0]
    nums[7] = [num for num in input if len(num) == 3][0]
    nums[8] = [num for num in input if len(num) == 7][0]

    aaaa = nums[7] - nums[1]

    # Get 2, 3, and 5 which all share aaaa, dddd and gggg
    five_segment_nums = [num for num in input if len(num) == 5]
    # Get just dddd and gggg
    dddd_and_gggg = set.intersection(*five_segment_nums) - aaaa
    dddd = nums[4].intersection(dddd_and_gggg)
    gggg = dddd_and_gggg - dddd

    nums[0] = [num for num in input if len(num) == 6 and num.intersection(dddd) == set()][0]

    six_and_nine = [num for num in input if len(num) == 6 and num != nums[0]]
    nums[9] = [num for num in six_and_nine if nums[1].issubset(num)][0]
    nums[6] = [num for num in six_and_nine if num != nums[9]][0]
    cccc = nums[1] - nums[6]
    ffff = nums[1] - cccc
    bbbb = nums[4] - cccc - dddd - ffff
    eeee = nums[6] - aaaa - bbbb - dddd - ffff - gggg
    nums[2] = aaaa | cccc | dddd | eeee | gggg
    nums[3] = aaaa | cccc | dddd | ffff | gggg
    nums[5] = aaaa | bbbb | dddd | ffff | gggg

    num = ""
    for out in outputs[i]:
        num += str(nums.index(set(out)))

    sum += int(num)

print(sum)
