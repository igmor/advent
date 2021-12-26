import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce
from roaringbitmap import RoaringBitmap, MultiRoaringBitmap

Cuboid = list[list[int]]

def p22_1(cubs) -> int:
    nc = 0
    for i in range(101):
        for j in range(101):
            nc += num_cubs(cubs[i][j])
    return nc

def num_cubs(c: int):
    count = 0
    while (c):
        count += c & 1
        c >>= 1
    return count
 

def p22_2(lines: list[str]) -> int:
    res = RoaringBitmap()
    n = 130000

    cubs = [[0 for i in range(n)] for j in range(n)]

    for l in lines:
        on_off, coords = l.strip().split()
        x, y, z = coords.split(',')
        _, x = x.split('=')
        x1, x2 = x.split('..')
        x1, x2 = min(int(x1), int(x2))+n, max(int(x1), int(x2))+n
        _, y = y.split('=')
        y1, y2 = y.split('..')
        y1, y2 = min(int(y1), int(y2))+n,  max(int(y1), int(y2))+n
        _, z = z.split('=')
        z1, z2 = z.split('..')
        z1, z2 = min(int(z1), int(z2))+n, max(int(z1), int(z2))+n
        print(x1,x2,y1,y2,z1,z2)
        lo = x1*n + y1
        hi = (x2+1)*n + y2 + 1
        print(lo, hi)
        res = res | RoaringBitmap(range(lo, hi))
                
    return len(res)

def to_bits(x1, x2: int) ->int:
    res = 0
    for i in range(x2-x1):
        res = (res << 1) | 1
    return res << x1

def parse(lines: list[str]):
    out = []
    cub = [[0 for i in range(101)] for j in range(101)]

    for l in lines:
        on_off, coords = l.strip().split()
        x, y, z = coords.split(',')
        _, x = x.split('=')
        x1, x2 = x.split('..')
        x1, x2 = max(-50, min(int(x1), int(x2))), min(50, max(int(x1), int(x2)))
        _, y = y.split('=')
        y1, y2 = y.split('..')
        y1, y2 = max(-50, min(int(y1), int(y2))), min(50, max(int(y1), int(y2)))
        _, z = z.split('=')
        z1, z2 = z.split('..')
        z1, z2 = max(-50, min(int(z1), int(z2))), min(50, max(int(z1), int(z2)))
        for i in range(x1+50, x2+51):
            for j in range(y1+50, y2+51):
                #print(x1,x2,y1,y2,z1,z2)
                c = to_bits(z1+50, z2+51)
                #print(z1,z2,bin(c))
                if on_off == 'on':
                    cub[i][j] = cub[i][j] | c
                else:
                    cub[i][j] = cub[i][j] & ~c
    return cub

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    cubs = parse(lines)
    print(p22_1(cubs))
    print(p22_2(lines))

    f.close()

