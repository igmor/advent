import argparse
import sys
import math
import resource
import copy
import bisect
from collections import defaultdict
from functools import reduce

def parse_snailfish_num(st, n):
    if not n:
        return st

    if n[0] == '[':
        st.append(list())
        return parse_snailfish_num(st, n[1:])
    elif n[0] == ']':
        if n[1:] == "":
            return st
        top = st.pop()
        if st:
            last = st[-1]
            last.append(top)
        return parse_snailfish_num(st, n[1:])
    elif n[0] == ',':
        return parse_snailfish_num(st, n[1:])
    else:
        top = st[-1]
        top.append(int(n[0]))
        return parse_snailfish_num(st, n[1:])

def explode(s, left, level, e, exploded):
    ns = 0
    if level == 4 and type(s[0]) == int and type(s[1]) == int and not e[0] and not e[1] and not exploded[0]:
        e[0] = s[0]
        e[1] = s[1]
        exploded[0] = True
        return 1
    if level == 1 and exploded[0] and e[0]:
        e[0] = None
    for i in range(len(s)):
        if type(s[i]) == list:
            ns = explode(s[i], left, level+1, e, exploded)
            if ns == 1:
                s[i] = 0
                continue
        if type(s[i]) == int and not exploded[0]:
            #print("left", s)
            left[0] = (s, i)
        if type(s[i]) == int and e[1]:
            s[i] += e[1]
            e[1] = None
    if left[0] and exploded[0] and e[0]:
        if left[0][0] != s:
            idx = left[0][1]
            left[0][0][idx] += e[0]
            e[0] = None
            left = [None]
    return 0

    
def split(s):
    for i in range(len(s)):
        if type(s[i]) == list:
            ns = split(s[i])
            if ns > 0:
                return ns
        if type(s[i]) == int:
            if s[i] >= 10:
                s[i] = [int(s[i]/2), int((s[i]+1)/2)]
                return 1
    return 0

def add(s1, s2):
    return [s1, s2]

def p18_1(lines: list[str]) -> int:
    res = None
    for l in lines:
        s_expr = parse_snailfish_num(list(), l.strip())[0]
        if res:
            print(res)
            print("+ ", s_expr)
            s_expr = add(res, s_expr)
        res = reduce(s_expr)
        print("=", s_expr)
        print("-----------------------------------------")

    print("RESULT: ", res)
    return mag(res)

def reduce(s_expr):
    while True:
        exploded = [False]
        ns = 0
        ns = explode(s_expr, [None], 0, [None, None], exploded)
        if exploded[0]:
            continue        
        ns = split(s_expr)
        if ns == 0:
            break
    return s_expr

def mag(s) -> int:
    if type(s) == int:
        return s
    return 3*mag(s[0]) + 2*mag(s[1])

def p18_2(lines: list[str]) -> int:
    max_mag = 0

    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            s_expr1 = parse_snailfish_num(list(), lines[i].strip())[0]
            s_expr2 = parse_snailfish_num(list(), lines[j].strip())[0]

            s_expr = add(s_expr1, s_expr2)
            s_expr = reduce(s_expr)
            mg = mag(s_expr)
            if mg > max_mag:
                max_mag = mg

    return max_mag

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    print(mag(p18_1(lines)))
    print(p18_2(lines))

    f.close()

