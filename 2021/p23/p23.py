import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

Cuboid = list[list[int]]
Cuboid2 = tuple[list[tuple[int, int]], int]

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
 

def p22_2(cuboids) -> int:
    #print(cuboids, len(cuboids))
    tot = 0
    for c, on in cuboids:
        if not c:
            continue
        v = (c[0][1] - c[0][0] + 1)*(c[1][1] - c[1][0] + 1)*(c[2][1] - c[2][0] + 1) * on
        tot += v
    return tot

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
                c = to_bits(z1+50, z2+51)
                if on_off == 'on':
                    cub[i][j] = cub[i][j] | c
                else:
                    cub[i][j] = cub[i][j] & ~c
    return cub

# segments [x01, x02] and [x11, x12]
def intersect_s(x01, x02, x11, x12) -> bool:
    return x02 >= x11 and x12 >= x01

def in_segment(s, x1, x2) -> bool:
    return s[0] >= x1 and s[1] <= x2

def intersect(c, cub):
    #print(out)
    cub, onoff = cub[0], cub[1]
    intersections = []
    cc, on = c[0], c[1]
    #print(cc, on)

    xi1 = cub[0][0]
    xi2 = cub[0][1]
    yi1 = cub[1][0]
    yi2 = cub[1][1]
    zi1 = cub[2][0]
    zi2 = cub[2][1]

    x1 = cc[0][0]
    x2 = cc[0][1]
    y1 = cc[1][0]
    y2 = cc[1][1]
    z1 = cc[2][0]
    z2 = cc[2][1]

    if intersect_s(xi1, xi2, x1, x2) and intersect_s(yi1, yi2, y1, y2) and intersect_s(zi1, zi2, z1, z2):

        px1 = max(xi1, x1)
        px2 = min(xi2, x2)

        py1 = max(yi1, y1)
        py2 = min(yi2, y2)

        pz1 = max(zi1, z1)
        pz2 = min(zi2, z2)

        sign = onoff * on
        if onoff == on:
            sign = -on
        elif on == 1 and onoff == -1:
            sign = 1

        return Cuboid2(([(px1, px2), (py1, py2), (pz1, pz2)], sign))
    return None

def parse2(lines: list[str]) -> list[tuple[Cuboid2, int]]:
    maxx = 0
    cuboids = []
    for l in lines:
        #print(l, len(cuboids))
        on_off, coords = l.strip().split()
        x, y, z = coords.split(',')
        _, x = x.split('=')
        x1, x2 = x.split('..')
        x1, x2 = min(int(x1)+maxx, int(x2)+maxx), max(int(x1)+maxx, int(x2)+maxx)
        _, y = y.split('=')
        y1, y2 = y.split('..')
        y1, y2 = min(int(y1)+maxx, int(y2)+maxx), max(int(y1)+maxx, int(y2)+maxx)
        _, z = z.split('=')
        z1, z2 = z.split('..')
        z1, z2 = min(int(z1)+maxx, int(z2)+maxx), max(int(z1)+maxx, int(z2)+maxx)
        sign = 1 if on_off == 'on' else -1
        c = Cuboid2(([(x1, x2), (y1, y2), (z1, z2)], sign))

        intersections = []
        for cuboid in cuboids:
            inter = intersect(c, cuboid)
            if inter is not None:
                intersections.append(inter)
        cuboids.extend(intersections)
        if on_off == 'on':
            cuboids.append(c)
    #print(cuboids)
    return cuboids

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    cubs = parse(lines)
    print(p22_1(cubs))
    cubs = parse2(lines)
    print(p22_2(cubs))

    f.close()

