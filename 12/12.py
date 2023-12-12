from functools import cache

lines = open("sample.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

gears = []
nums = []
for line in lines:
    s = line.split()
    gears.append(s[0])
    nums.append(tuple(s[1].split(',')))
    # Uncomment for Part 2
    # gears.append(4*(s[0]+'?') + s[0])
    # nums.append(tuple(s[1].split(',') * 5))

# Potential optimization: encase the function in the loop and only pass 
# indecies to decrease memory usage of the @cache. Not necessary with current hardware.
@cache
def opts(gear, num):
    # Base cases, solution is bad if there are sections left unaccounted for
    if not num: 
        return (False, 0) if '#' in gear else (True, 1)
    # Solution is bad if there are no gears left but still more #s
    if not gear:
        return (False, 0) if num else (True, 1)
    
    n = int(num[0])
    for i in range(len(gear)-n+1):
        # Must place a gear where we find a #, false if we can't place that
        if '#' == gear[i]:
            # Check for .s and make sure we don't have a # extending the section
            if '.' in gear[i:i+n] or ((len(gear) > i+n) and (gear[i+n] == '#')):
                return (False, 0)
            return opts(gear[i+n+1:], num[1:])

        # Return sum of placing the gear or moving on by one space
        elif not '.' in gear[i:i+n] and (len(gear) <= i+n or gear[i+n] != '#'):
            place = opts(gear[i+n+1:], num[1:])
            cont = (False, 0) if gear[i] == '#' else opts(gear[i+1:], num)
            return (place[0] or cont[0], (cont[1] if cont[0] else 0) + (place[1] if place[0] else 0))

    return (False, 0)

ret = 0

for i in range(len(gears)):
    # print(i, o:=opts(gears[i], nums[i])[1] )
    ret += opts(gears[i], nums[i])[1]

print(ret)