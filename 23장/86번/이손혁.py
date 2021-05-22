def stair(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return stair(n-1) + stair(n-2)
