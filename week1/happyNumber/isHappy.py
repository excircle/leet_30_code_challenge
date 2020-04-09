def isHappy(n: int) -> bool:
    t = 0
    while t != 1000000:
        e = sum([int(i)**2 for i in str(n)])
        if e == 1:
            return True
        t += 1
        n = e
    return False