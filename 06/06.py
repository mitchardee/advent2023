from math import sqrt


times = [54, 94, 65, 92]
dists = [302, 1476, 1029, 1404]

times = [54946592]
dists = [302147610291404]

# Sample values
# times = [7, 15, 30]
# dists = [9, 40, 200]
# times = [71530]
# dists = [940200]

product = 1

for i in range(len(times)):
    for j in range(times[i]):
        if (j * (times[i]-j)) > dists[i]:
            product *= times[i] + 1 - 2*j
            break
    print(product)

# Explicit solution?
print(sqrt(71530**2 - 4 * 940200))
print(sqrt(times[0]**2 - 4 * dists[0]))