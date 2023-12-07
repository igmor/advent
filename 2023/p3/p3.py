from typing import List, Tuple
import argparse

def touching(s: str, engine: List[List[str]], startd, i, j:int) -> bool:
    for k1 in [i-1, i+1]:
        for k2 in range(startd-1, j+1):
            if k1 >= 0 and k2 >= 0 and k1 < len(engine) and k2 < len(engine[k1]):
                print(engine[k1][k2], end='')
                if engine[k1][k2] != '.':
                    print(engine[k1][k2])
                    return True
            print('\n')
    k1 = i
    for k2 in [startd-1, j]:
        if k1 >= 0 and k2 >= 0 and k1 < len(engine) and k2 < len(engine[k1]):
            if engine[k1][k2] != '.':
                print(engine[k1][k2])
                return True
    return False

def p12(engine: List[List[str]]) -> int:
    total = 0
    d = ''
    startd = -1
    for i, s in enumerate(engine):
        for j, c in enumerate(s):
            if c.isdigit():
                d += c
                if startd < 0:
                    startd = j
            else:
                if d != '':
                    #print(d)
                    if touching(d, engine, startd, i, j):
                        total += int(d)
                    d = ''
                    startd = -1
        if d != '':
            if touching(d, engine, startd, i, len(s)):
                total += int(d)
            d = ''
            startd = -1
        
    return total

def p21(engine: List[List[str]]) -> int:
    total = 0

    d = ''
    startd = -1
    dnum = {}

    for i, s in enumerate(engine):
        for j, c in enumerate(s):
            if c.isdigit():
                d += c
                if startd < 0:
                    startd = j
            else:
                if d != '':
                    #print(d)
                    for k in range(startd, j):
                        if (i, k) not in dnum:
                            dnum[(i, k)] = int(d)
                    d = ''
                    startd = -1
        if d != '':
            for k in range(startd, j):
                if (i, k) not in dnum:
                    dnum[(i, k)] = int(d)
            d = ''
            startd = -1

    print(dnum)
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j] != '.' and not engine[i][j].isdigit(): # symbol
                circle = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                num_d = set([])

                for kc in range(len(circle)):
                    k = circle[kc]
                    if k[0] >= 0 and k[1] >= 0 and k[0] < len(engine) and k[1] < len(engine[k[0]]):
                        if engine[k[0]][k[1]].isdigit():
                            num_d.add(dnum[(k[0], k[1])])
                    print(num_d)
                if len(num_d) == 2:
                    mul = 1
                    for d in num_d:
                        mul *= d
                    total += mul
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    engine = []
    for l in lines:
        l = l.replace('\n','')
        engine.append(list(l))
    f.close()
    #print(p12(engine))
    print(p21(engine))


