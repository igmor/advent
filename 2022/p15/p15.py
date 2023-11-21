from typing import List, Tuple, Callable
import argparse
import sys
import ast
import functools

BSType = Tuple[Tuple[int, int], Tuple[int, int]]

def generate_grid(result: List[BSType], minx, maxx, miny, maxy: int) -> List[List[str]]:
    grid = [['.' for i in range(0, maxx + 2)] for j in range(0, maxy + 2)]
    for bs in result:
        s = bs[0]
        b = bs[1]
        grid[s[1]][s[0]] = 'S'
        grid[b[1]][b[0]] = 'B'
    return grid

def draw_grid(grid: List[List[str]], minx, maxx, miny, maxy: int):
     for i in range(0, maxy + 1):
        for j in range(minx, maxx + 1):
            print(grid[i][j], end='')
        print('')

def manh(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
   
def unite_pair(pair):
    if pair[0][0] <= pair[1][0] <= pair[0][1]:
        if pair[0][1] > pair[1][1]:
            return pair[0]
        elif pair[0][1] <= pair[1][1]:
            return [pair[0][0], pair[1][1]]
    else:
        return pair
    
def union_of_sections(sections):
    sections = sorted(sections)
    for_ret = list()
    while len(sections) > 1:
        one = sections.pop(0)
        two = sections.pop(0)
        pair = [one, two]
        united_pair = unite_pair(pair)
        try:
            len(united_pair[0])
            for_ret.append(united_pair[0])
            sections = [two] + sections
        except TypeError as err:
            sections = [united_pair] + sections
    for_ret.extend(sections)
    return for_ret

def p11(result: List[BSType], minx, maxx, miny, maxy: int) -> int:
    #grid = generate_grid(result, minx, maxx, miny, maxy)
    #draw_grid(grid, minx, maxx, miny, maxy)

    ty = 2000000
    out = []
    for s, b in result:
        md = manh(s, b)
        fromx = max(minx, s[0] - md)
        tox = min(maxx, s[0] + md)
        fromy = max(miny, s[1] - md)
        toy = min(maxy, s[1] + md)
        left = None
        right = None
        for x in range(fromx, s[0]):
            if manh((x, ty), s) <= md:
                left = x
                break
        for x in range(s[0], tox+10000000):
            if manh((x, ty), s) <= md:
                right = x
            else:
                break
        if left:
            out.append((left, right))

    print(out)
    un = union_of_sections(out)
    print(un)
    n = 0
    for s in un:
        n += s[1] - s[0] + 1
    #draw_grid(grid, minx, maxx, miny, maxy)

    # for x in range(maxx):
    #     if grid[ty][x] == '#' or grid[ty][x] == 'S' or grid[ty][x] == 'B':
    #         n += 1

    set_of_p = set()
    for s, b in result:
        set_of_p.add(s)
        set_of_p.add(b)

    for p in set_of_p:        
        if p[1] == ty:
            print(p)
            n -= 1

    return n

def p12(result: List[List[Tuple[int, int]]], minx, maxx, miny, maxy: int) -> int:
    #grid = generate_grid(result, minx, maxx, miny, maxy)
    #draw_grid(grid, minx, maxx, miny, maxy)

    segments = []
    out = []

    for ty in range(0, 4000000):
        segments = []
        for s, b in result:
            md = manh(s, b)
            if s[1] - md <= ty <= s[1] + md:
                d = md - abs(ty - s[1])
                segments.append((s[0] - d, s[0] + d + 1))
        un = union_of_sections(segments)
        if len(un) > 1:
            return un[0][1]*4000000 + ty
    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    result = []
    minx, maxx, miny, maxy = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize
    for l in lines:
        l = l.replace('\n', '')
        sensor, beacon = l.split(':')
        sensor = sensor.replace('Sensor at ', '')
        beacon = beacon.replace('closest beacon is at ', '')
        print(sensor, beacon)
        sx, sy = sensor.split(',')
        sx = int(sx.strip().replace('x=', ''))
        sy = int(sy.strip().replace('y=', ''))
        bx, by = beacon.split(',')
        bx = int(bx.strip().replace('x=', ''))
        by = int(by.strip().replace('y=', ''))
        if sx < minx:
            minx = sx
        if sx > maxx:
            maxx = sx
        if sy < miny:
            miny = sy
        if sy > maxy:
            maxy = sy
        if bx < minx:
            minx = bx
        if bx > maxx:
            maxx = bx
        if by < miny:
            miny = by
        if by > maxy:
            maxy = by

        result.append(((sx, sy), (bx, by)))
    print(result)

    #print(p11(result, minx, maxx, miny, maxy))
    print(p12(result, minx, maxx, miny, maxy))
