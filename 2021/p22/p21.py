import argparse
import sys
import math
import resource
import copy
import random
import bisect
from collections import defaultdict
from functools import reduce
from sortedcontainers import SortedDict

def p24_1(p1, p2: int) -> int:
    score1 = 0
    score2 = 0
    d1 = 6
    d2 = 15
    ndie = 0
    while True:
        p1 = (p1 + d1) % 10
        if p1 == 0:
            p1 = 10

        score1 += p1
        ndie += 3

        if score1 >= 1000:
            break
        p2 = (p2 + d2) % 10
        if p2 == 0:
            p2 = 10

        score2 += p2
        ndie += 3
        if score2 >= 1000:
            break
        d1 += 18
        d2 += 18
        print("p1: ", score1, p1, "p2: ", score2, p2, "ndie: ", ndie)
        
    print("p1: ", score1, p1, "p2: ", score2, p2, "ndie: ", ndie)
    return min(score1, score2) * ndie
    
def score(p1, p2, s1, s2, die) -> tuple[int, int]:
    if len(die) % 3 == 0:
        if s1 >= 21:
            return (1, 0)
        if s2 >= 21:
            return (0, 1)
        
    for d in [1, 2, 3]:
        if p1 + d > 10:
            s1 += p1 + d - 10
        else:
            s1 += p1 + d - 10


def p24_2(p1, p2:int) -> int:
    d = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
    scores = SortedDict([((p1, p2, 0, 0), (0, 0))])
    tot1 = 0
    tot2 = 0
    do_not_add_back = False
    while len(scores) > 0:
        ((p1, p2, s1, s2), (nu1, nu2)) = scores.popitem(0)
        if s1 >= 21:
            tot1 += nu1
            continue
        if s2 >= 21:
            tot2 += nu2
            continue

        for k1, v1 in  d.items():
            for k2, v2 in d.items():
                p1 = (p1 + k1) % 10
                if p1 == 0:
                    p1 = 10
                s1 += p1
                if s1 >= 21:
                    tot1 += v1
                    continue
                p2 = (p2 + k2) % 10
                if p2 == 0:
                    p2 = 10
                s2 += p2
                if s2 >= 21:
                    tot2 += v2
                    continue
                print(s1, s2)
                if scores.get((p1, p2, s1, s2)):
                    (v01, v02) = scores[(p1, p2, s1, s2)]
                    scores[(p1, p2, s1, s2)] = (v01+v1, v02+v2)
                else:
                    scores[(p1, p2, s1, s2)] = (v1, v2)
                    
        print(scores)
    print(tot1,tot2)
    return 0

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    #print(p24_1(7, 3))
    print(p24_2(7, 3))

