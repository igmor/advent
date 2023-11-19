from typing import List, Tuple, Callable
import argparse
import sys
import ast
import functools

start = (500, 0)

def generate_grid(result: List[List[Tuple[int, int]]], minx, maxx, miny, maxy: int) -> List[List[str]]:
    grid = [['.' for i in range(0, maxx + 2)] for j in range(0, maxy + 2)]
    for s in result:
        s1 = s[0]
        grid[s1[1]][s1[0]] = '#'
        i = 1
        while i < len(s):
            cur = s[i]
            if cur[0] == s1[0]:
                for y in range(min(s1[1], cur[1]), max(s1[1], cur[1])+1):
                    grid[y][cur[0]] = '#'
            elif cur[1] == s1[1]:
                for x in range(min(s1[0], cur[0]), max(s1[0], cur[0])+1):
                    grid[cur[1]][x] = '#'
            i += 1
            s1 = cur
    return grid

def draw_grid(grid: List[List[str]], minx, maxx, miny, maxy: int):
     for i in range(0, maxy + 1):
        for j in range(minx, maxx + 1):
            print(grid[i][j], end='')
        print('')

   
def p11(result: List[List[Tuple[int, int]]], minx, maxx, miny, maxy: int) -> int:
    grid = generate_grid(result, minx, maxx, miny, maxy)
    draw_grid(grid, minx, maxx, miny, maxy)

    n = 0
    cur = None
    while True:
        if cur:
            print(cur)
            if cur[0] > maxx or cur[0] < minx:
                break
            if grid[cur[1]+1][cur[0]] == '.':
                cur[1] +=1
            elif grid[cur[1]+1][cur[0]] == '#' or grid[cur[1]+1][cur[0]] == 'o':
                if grid[cur[1]+1][cur[0]-1] == '.':
                    cur[0] -= 1
                    cur[1] += 1
                elif grid[cur[1]+1][cur[0]+1] == '.':
                    cur[0] += 1
                    cur[1] += 1
                else:
                    grid[cur[1]][cur[0]] = 'o'
                    n += 1
                    cur = None
        else:
            cur = [start[0], start[1]]      
    draw_grid(grid, minx, maxx, miny, maxy)
    return n

def p12(result: List[List[Tuple[int, int]]], minx, maxx, miny, maxy: int) -> int:
    grid = generate_grid(result, 0, maxx*2, 0, maxy*2)
    draw_grid(grid, minx, maxx, miny, maxy)

    n = 0
    cur = None
    while True:
        if cur:
            print(cur)
            if cur[1]+1 == maxy + 1:
                if grid[cur[1]+1][cur[0]-1] == '.':
                    grid[cur[1]+1][cur[0]-1] = 'o'
                elif grid[cur[1]+1][cur[0]+1] == '.':
                    grid[cur[1]+1][cur[0]+1] = 'o'
                else:
                    grid[cur[1]][cur[0]] = 'o'
                n += 1
                cur = None
                continue
            if grid[cur[1]+1][cur[0]] == '.':
                cur[1] +=1
            elif grid[cur[1]+1][cur[0]] == '#' or grid[cur[1]+1][cur[0]] == 'o':
                if grid[cur[1]+1][cur[0]-1] == '.':
                    cur[0] -= 1
                    cur[1] += 1
                elif grid[cur[1]+1][cur[0]+1] == '.':
                    cur[0] += 1
                    cur[1] += 1
                else:
                    grid[cur[1]][cur[0]] = 'o'
                    n += 1
                    if cur[0] == 500 and cur[1] == 0:
                        break
                    cur = None
        else:
            cur = [start[0], start[1]]      
    draw_grid(grid, minx-20, maxx+20, miny, maxy+3)
    return n

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
        segments = l.split('->')
        pairs = []
        for s in segments:
            x, y = s.strip().split(',')
            x, y = int(x), int(y)
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
            pairs.append((x, y))
        result.append(pairs)
    print(result)

    print(p11(result, minx, maxx, miny, maxy))
    print(p12(result, minx, maxx, miny, maxy))
