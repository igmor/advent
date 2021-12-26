import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

Algo = list[int]
Image = list[list[int]]

def p20_1(img: Image, algo: Algo) -> int:
    out = img
    for i in range(2):        
        out = render_output(out, algo)
        
    print(len(out), len(out[0]))
    return num_lit_pixels(out, 0)


def p20_2(img: Image, algo: Algo) -> int:
    out = img
    for i in range(100):       
        print(i) 
        out = render_output(out, algo)
        
    f = open("out", 'w')
    #print('----------------------------------------')
    for i in range(len(out)):
        f.write("".join(out[i]))
        f.write('\n')

    f.close()
    print(len(out), len(out[0]))
    return num_lit_pixels(out, 7)

def num_lit_pixels(img: Image, padding:int) -> int:
    nlit = 0
    for i in range(padding,len(img)-padding):
        for j in range(padding, len(img[0])-padding):
            if img[i][j] == '#':
                nlit += 1
    return nlit

def in_range(idx, min_r, max_r) -> bool:
    if idx >= min_r and idx < max_r:
        return True
    return False

def to_number(s: str) -> int:
    return int(s, 2)

def render_output(img: Image, algo: Algo) -> Image:
    out = [['.' for i in range(len(img) + 12)] for j in range(len(img[0])+12)]
    for i in range(len(out)):
        for j in range(len(out[0])):
            s = ''
            for k1 in [-1, 0, 1]:
                for k2 in [-1, 0, 1]:
                    #print(i+k1-1, j+k2-1)
                    c = (img[i+k1-6][j+k2-6] if in_range(i+k1-6, 0, len(img)) and in_range(j+k2-6, 0, len(img[0])) else '.')
                    s += '0' if c == '.' else '1'
            if i == 2 and j == 2:
                print("index in algo: ", s, to_number(s))
            out[i][j] = algo[to_number(s)]
    #print('----------------------------------------')
    #for i in range(len(out)):
    #    print("".join(out[i]))

    return out


def parse(lines: list[str]) -> tuple[Image, Algo]:
    img = []
    algo = list(lines[0].strip())
    for l in lines[2:]:
        img.append(list(l.strip()))
    return img, algo

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    img, algo = parse(lines)
    #print(img, algo)
    print(p20_1(img, algo))
    print(p20_2(img, algo))

    f.close()

