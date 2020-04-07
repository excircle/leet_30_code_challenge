from typing import List

def singleNumber(n: List[int]) -> int:
    d = {}
    for v in n:
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
    r = None
    for k, v in d.items():
        if v == 1:
            r = k
    return r

l = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,10]

print(singleNumber(l))