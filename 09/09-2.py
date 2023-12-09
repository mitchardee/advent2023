lines = open("input.txt").readlines()

nums = [[int(x) for x in line.strip().split()] for line in lines]
# print(nums)
ret = 0
for l in nums:
    pyramid = [l]
    while any(pyramid[-1]) and len(pyramid[-1]) > 1:
        pyramid.append([pyramid[-1][i+1] - pyramid[-1][i] for i in range(len(pyramid[-1]) - 1)])
    # print(pyramid)
    ret += l[0]
    for i, line in enumerate(pyramid[1:], 1):
        ret += line[0] * (-1) ** i

print(ret)