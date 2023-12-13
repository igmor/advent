from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
from math import gcd
import sys
import bisect
import argparse
import functools


def diff1(l: List[int]) -> int:
    if all(i == l[0] for i in l):
        return l
    
    r = diff1([l[i+1] - l[i] for i in range(len(l)-1)])
    return l + [l[-1] + r[-1]]

def p12(history: List[List[int]]) -> int:
    total = 0
    for h in history:
        r = diff1(h)
        total += r[-1]
    return total

def diff2(l: List[int]) -> int:
    if all(i == l[0] for i in l):
        return l
    
    r = diff2([l[i+1] - l[i] for i in range(len(l)-1)])
    print([l[0] - r[0]] + l)
    return [l[0] - r[0]] + l

def p21(history: List[List[int]]) -> int:
    total = 0
    for h in history:
        r = diff2(h)
        total += r[0]
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    history = []
    for line in lines:
        l = line.strip().replace('\n', '')
        l = l.split()
        history.append([int(x) for x in l])
    f.close()
    print(history)
    print(p12(history))
    print(p21(history))
    