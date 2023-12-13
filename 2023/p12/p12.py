from typing import List, Tuple, Dict
from sortedcontainers import SortedSet
from collections import defaultdict
from math import gcd
import sys
import re
import bisect
import argparse
import functools

rep = "(\\#{n})"

cache = {}

def spring(s, p: str, g: List[str], gi:int, ggi: int, result: List[int]) -> int:
    key = (s, gi, ggi)
    if key in cache:
        return cache[key]
    if gi >= len(g):
        return 0
    
    if gi < len(g) and ggi > int(g[gi]):
        return 0
    
    if len(s) == 0:
        if gi == len(g)-1 and (ggi == int(g[gi]) or ggi == -1):
            #print(p, g, gi, ggi)
            result[0] += 1
            return 1
        return 0
    
    num = 0
    c = s[0]
    if s[0] == '.':
        if ggi == -1 or ggi == int(g[gi]):
            num = spring(s[1:], p + c, g, gi, -1, result)
        return num
    
    if c == '#':
        if ggi == -1:
            num += spring(s[1:], p + c, g, gi+1, 1, result) # start a new group
        else: # within a group
            num += spring(s[1:], p + c, g, gi, ggi+1, result)
    elif c == '?':
        if ggi == -1:
            num += spring(s[1:], p + '#',g, gi+1, 1, result)
        else:
            num += spring(s[1:], p + '#', g, gi, ggi+1, result)
        
        #print(s, gi, ggi)
        if ggi == -1 or ggi == int(g[gi]):
            num += spring(s[1:], p + '.', g, gi, -1, result)

    cache[key] = num
    return num

def spring_regex(s, p: str, regex: any) -> int:
    if '?' not in s:
        if regex.match(p+s):
            #print(p, s, regex)
            return 1
        return 0
    
    if s[0] == '.' or s[0] == '#':
        return spring_regex(s[1:], p + s[0], regex)
    if s[0] == '?':
        return spring_regex(s[1:], p + '#', regex) + spring_regex(s[1:], p + '.', regex)

def p12(grid: List[Tuple[str, List[int]]]) -> int:
    total = 0
    total1 = 0
    for g in grid:
        result = [0]
        num = spring(g[0], '', g[1], -1, -1, result)
        total += num
    return total, total1

def p21(grid: List[List[str]]) -> int:
    total = 0
    total1 = 0
    for (i, g) in enumerate(grid):
        result = [0]
        sp = '?'.join([g[0] for i in range(5)])
        groups = g[1]*5
        #print(sp, groups)
        cache.clear()
        num = spring(sp, '', groups, -1, -1, result)
        total += num
        print(i, num, total)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    grid = []
    for line in lines:
        l = line.strip().replace('\n', '')
        sp, groups = l.split()
        groups = groups.split(',')
        grid.append((sp.strip(), groups))
    f.close()
    print(grid)
    print(p12(grid))
    print(p21(grid))
    