nums = []

with open("input.txt") as f:
    for l in f:
        nums.append(l)

most_common = []
least_common = []

for i in range(len(nums[0].strip())):
    lst = [num[i] for num in nums]
    lst = sorted(lst, reverse=True)
    most_common_num = max(lst, key=lst.count)
    most_common.append(most_common_num)
    least_common.append('0' if most_common_num == '1' else '1')

num_1 = int(''.join(most_common), 2)
num_2 = int(''.join(least_common), 2)

print(num_1 * num_2)

nums_most = nums
nums_least = nums

i = 0
while len(nums_most) > 1:
    lst = [num[i] for num in nums_most]
    lst = sorted(lst, reverse=True)
    most_common_num = max(lst, key=lst.count)
    nums_most = [num for num in nums_most if num[i] == most_common_num]
    i += 1

i = 0
while len(nums_least) > 1:
    lst = [num[i] for num in nums_least]
    lst = sorted(lst)
    least_common_num = min(lst, key=lst.count)
    nums_least = [num for num in nums_least if num[i] == least_common_num]
    i += 1

print(int(nums_most[0].strip(), 2) * int(nums_least[0].strip(), 2))
