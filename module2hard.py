import random

rand_num = random.randrange(3, 20)
range_rand_nums = list(range(1, rand_num + 1))
length = len(range_rand_nums)

res_list = []

for i in range(length - 1):
    x = range_rand_nums[i]

    for j in range(length - 1):
        y = range_rand_nums[j]
        if (x != y) and rand_num % (x + y) == 0 and (not (y, x) in res_list):
            res_list.append((x, y))

result_str = ""
for r in res_list:
    result_str += "".join(map(str, r))

print(rand_num)
print(result_str)