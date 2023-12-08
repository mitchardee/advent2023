lines = open("sample.txt").readlines()

hands = [line.strip().split() for line in lines]
vals = {'2':0, '3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, 'T':8, 'J':9, 'Q':10, 'K':11, 'A':12}

def k(s):
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    d = list(d.values())

    hand = 0
    if 5 in d:
        hand = 7
    elif 4 in d:
        hand = 6
    elif 3 in d:
        if 2 in d:
            hand = 5
        else:
            hand = 4
    elif 2 in d:
        if d.count(2) == 2:
            hand = 3
        else:
            hand = 2
    else:
        hand = 1

    ret = 0
    for c in s:
        ret *= 13
        ret += vals[c]
    return ret + (13**5) * hand

hands.sort(key=lambda hand: k(hand[0]))

ret = 0

for i, hand in enumerate(hands, 1):
    ret += i * int(hand[1])

print(ret)