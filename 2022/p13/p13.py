from typing import List, Tuple, Callable
import argparse
import sys
import ast
import functools

def order(p1: List, p2: List) -> int:
    #print(p1, ':', p2)
    for i in range(max(len(p1), len(p2))):
        if i >= len(p1):
            return 1
        if i >= len(p2):
            return -1
        e1 = p1[i]
        e2 = p2[i]
        ret = 0
        if type(e1) == int and type(e2) == int:
            if e1 < e2:
                return 1
            elif e1 > e2:
                return -1
        elif type(e1) == int and type(e2) == list:
            ret = order([e1], e2)
        elif type(e1) == list and type(e2) == int:
            ret = order(e1, [e2])
        else:
            ret = order(e1, e2)
        if ret != 0:
            return ret
    return 0

def p11(result: List[Tuple[List, List]]) -> int:
    s = 0
    for i, p in enumerate(result):
       print('__________________________')
       if order(p[0], p[1]) >=0 :
           print(i+1)
           s += (i + 1)
    return s

def p12(result: List[Tuple[List, List]]) -> int:
    result.append(([[2]], [[6]]))
    ll = []

    for p1, p2 in result:
        ll.append(p1)
        ll.append(p2)

    sorted_ll = sorted(ll, key=functools.cmp_to_key(order), reverse=True)
    i1 = 0
    i2 = 0
    for i, p in enumerate(sorted_ll):
        if p == [[2]]:
            i1 = i + 1
        if p == [[6]]:
            i2 = i + 1
    print(sorted_ll)
    return i1 * i2

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    result = []
    for i in range(0, len(lines)-3, 3):
        l1 = lines[i].replace('\n', '')
        l2 = lines[i+1].replace('\n', '')
        result.append((ast.literal_eval(l1), ast.literal_eval(l2)))
    #print(result)
    s_pairs = [pair.split("\n") for pair in open("input.txt").read().split("\n\n")]
    pairs = list(map(lambda p: [eval(i) for i in p], s_pairs))

    print(p11(pairs))
    print(p12(pairs))
