prev = None
increases = 0

with open("input.txt") as f:
    for l in f:
        l = int(l)

        if prev is not None and l > prev:
            increases += 1

        prev = l

print(f"# of increases: {increases}")

nums = []
increases = 0

with open("input.txt") as f:
    for l in f:
        l = int(l)

        nums.append(l)

prev = nums[0] + nums[1] + nums[2]

for i in range(3, len(nums)):
    res = nums[i - 2] + nums[i - 1] + nums[i]
    if res > prev:
        increases += 1
    prev = res

print(f"# of increases: {increases}")
