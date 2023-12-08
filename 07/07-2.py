lines = open("input.txt").readlines()

hands = [line.strip().split() for line in lines]
vals = {'J': 0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'Q':10, 'K':11, 'A':12}

def k(s):
    dic = dict()
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    j = dic.pop('J') if 'J' in dic else 0
    d = sorted(list(dic.values()))
    m = d.pop() if d else 0
    hand = 0

    if m + j == 5:
        hand = 7
    elif m + j == 4:
        hand = 6
    elif m + j == 3:
        if d[-1] == 2:
            hand = 5
        else:
            hand = 4
    elif m + j == 2:
        if d[-1] == 2:
            hand = 3
        else:
            hand = 2
    else:
        hand = 1

    for c in s:
        hand *= 13
        hand += vals[c]
    return hand

hands.sort(key=lambda hand: k(hand[0]))

ret = 0

for i, hand in enumerate(hands, 1):
    ret += i * int(hand[1])

print(ret)