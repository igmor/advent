import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce
from scipy.sparse import lil_matrix

Cuboid = list[list[int]]
Cuboid2 = list[tuple[int, int]]

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
 

def p22_2(m) -> int:
    print(m)
    return 0

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

# segments [x01, x02] and [x11, x12]
def intersect(x01, x02, x11, x12) -> bool:
    return x02 >= x11 and x12 >= x01

def in_segment(s, x1, x2) -> bool:
    return s[0] >= x1 and s[1] <= x2

def add(out, cub, onoff):
    crossed = False

    for i in range(len(out)):

        c, on = out[i]
        if not c:
            continue

        xi1 = cub[0][0]
        xi2 = cub[0][1]
        yi1 = cub[1][0]
        yi2 = cub[1][1]
        zi1 = cub[2][0]
        zi2 = cub[2][1]

        x1 = c[0][0]
        x2 = c[0][1]
        y1 = c[1][0]
        y2 = c[1][1]
        z1 = c[2][0]
        z2 = c[2][1]

        if intersect(xi1, xi2, x1, x2) and intersect(yi1, yi2, y1, y2) and intersect(zi1, zi2, z1, z2):
            if in_segment((xi1, xi2), x1, x2) \
            and in_segment((yi1, yi2), y1, y2) \
            and in_segment((zi1, zi2), z1, z2) and on == onoff:
                continue

            if in_segment((x1, x2), xi1, xi1) \
            and in_segment((y1, y2), yi1, yi1) \
            and in_segment((z1, z2), zi1, zi1) and on == onoff:
                out[i] = (Cuboid2([(xi1, xi1), (yi1, yi1), (zi1, zi1)]), on)
                continue

            px1 = min(xi1, x1)
            px2 = max(xi1, x1)
            px3 = min(xi2, x2)
            px4 = max(xi2, x2)

            py1 = min(yi1, y1)
            py2 = max(yi1, y1)
            py3 = min(yi2, y2)
            py4 = max(yi2, y2)

            pz1 = min(zi1, z1)
            pz2 = max(zi1, z1)
            pz3 = min(zi2, z2)
            pz4 = max(zi2, z2)

            for s1 in [(px1, px2), (px2, px3), (px3, px4)]:
                for s2 in [(py1, py2), (py2, py3), (py3, py4)]:
                    for s3 in [(pz1, pz2), (pz2, pz3), (pz3, pz4)]:

                        if not in_segment(s1, xi1, xi2) and not in_segment(s1, x1, x2):
                            continue
                        if not in_segment(s2, yi1, yi2) and not in_segment(s2, y1, y2):
                            continue
                        if not in_segment(s3, zi1, zi2) and not in_segment(s3, z1, z2):
                            continue

                        cc = Cuboid2([s1, s2, s3])
                        #in_segment(s1, xi1, xi2) and in_segment(s1, x1, x2) and in_segment(s2, yi1, yi2) and in_segment(s2, y1, y2) and in_segment(s3, zi1, zi2) and in_segment(s3, z1, z2):
                        out.append((cc, onoff))

            out[i] = (None, on)
            crossed = True
    if not crossed:
        out.append((cub, onoff))


def parse2(lines: list[str]) -> list[tuple[Cuboid2, int]]:
    out = []

    maxx = 0
    for l in lines:
        print(l, len(out))
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
        add(out, Cuboid2([(x1, x2), (y1, y2), (z1, z2)]), 1 if on_off == 'on' else 0)

    return out

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

