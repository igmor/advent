import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

d = defaultdict(int)

def p17_1(x1,x2,y1,y2:int) -> int:
    x_low = int((-1 + math.sqrt(1+4*2*x1))/2)
    x_high = int((-1 + math.sqrt(1+4*2*x2))/2)

    print(x1,x2,y1,y2)
    print(x_low, x_high)

    maxy = 0

    for d1 in range(x_low, x_high+1):
        for d2 in range(200):
            x = d1
            y = d2

            d11 = d1
            d22 = d2

            y_high = 0
            while True:
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    #print(x, y, d1, d2, y_high)
                    if y_high > maxy:
                        maxy = y_high

                    break
                if x > x2 or y < y1:
                    x = 0
                    y = 0
                    break
                if d11 > 0:
                    d11 -= 1
                elif d11 < 0:
                    d11 += 1
                d22 -= 1
                x += d11
                y += d22
                if y > y_high:
                    y_high = y


    return maxy

def p17_2(x1,x2,y1,y2:int) -> int:
    x_low = int((-1 + math.sqrt(1+4*2*x1))/2)
    x_high = int((-1 + math.sqrt(1+4*2*x2))/2)

    print(x1,x2,y1,y2)
    print(x_low, x_high)

    maxy = 0

    out = []
    for d1 in range(1000):
        for d2 in range(-200, 200):
            x = d1
            y = d2

            d11 = d1
            d22 = d2

            y_high = 0
            while True:
                #if d1 == 6 and d2 == 3:
                #    print(x,y)
                if x >= x1 and x <= x2 and y >= y1 and y <= y2:
                    print(x, y, d1, d2, y_high)
                    out.append((x, y, d1, d2, y_high))
                    if y_high > maxy:
                        maxy = y_high

                    break
                if x > x2 or y < y1:
                    x = 0
                    y = 0
                    break
                if d11 > 0:
                    d11 -= 1
                elif d11 < 0:
                    d11 += 1
                d22 -= 1
                x += d11
                y += d22
                if y > y_high:
                    y_high = y

    print(out)
    return len(out)

def parse(lines: list[str]) -> tuple[int, int, int, int]:
    x1, x2 = lines[0].strip().split(',')
    y1, y2 = lines[1].strip().split(',')
    return int(x1), int(x2), int(y1), int(y2)

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    x1, x2, y1, y2 = parse(lines)
    print(p17_1(x1, x2, y1, y2))
    print(p17_2(x1, x2, y1, y2))

    f.close()

