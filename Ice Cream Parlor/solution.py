def whatFlavors(cost, money):
    remains = dict()
    for index, c in enumerate(cost):
        if c not in remains:
            remains[money - c] = index + 1
        else:
            print(remains[c], index + 1)

# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/forum/comments/765508