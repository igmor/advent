import argparse
from collections import defaultdict

def print_octo(octos: list[list[int]]):
    for l in octos:
        print(''.join(map(str, l)))

def flash(l: list[tuple[int, int]], octos: list[list[int]]):
    n = 0
    flashed = set()
    while l:
        i, j = l[0]
        l = l[1:]
        octos[i][j] = 0
        flashed.add((i, j))
        n += 1
        for k1 in range(i-1, i+2):
            for k2 in range(j-1, j+2):
                if k1 >= 0 and k1 < len(octos) and k2 >= 0 and k2 < len(octos[0]):
                    if (k1, k2) in flashed:
                        continue
                    if k1 == i and k2 == j:
                        continue
                    octos[k1][k2] += 1
                    if octos[k1][k2] == 10:
                        l.append((k1, k2))
    return n

def p11_1(octos: list[list[int]]):
    n = 0
    for k in range(195):
        flash_candidates = []
        for i in range(len(octos)):
            for j in range(len(octos[0])):
                octos[i][j] += 1
                if octos[i][j] == 10:
                    flash_candidates.append((i, j))
        n += flash(flash_candidates, octos)
        print("---------------", n)
        print_octo(octos)

    return n

def p11_2(octos: list[list[int]]):
    for k in range(1000):
        flash_candidates = []
        for i in range(len(octos)):
            for j in range(len(octos[0])):
                octos[i][j] += 1
                if octos[i][j] == 10:
                    flash_candidates.append((i, j))
        n = flash(flash_candidates, octos)
        print("---------------", n)
        print_octo(octos)
        if n == len(octos) * len(octos[0]):
            return k + 1

    return n

def parse(lines: list[str]) -> list[list[int]]:
    out = []
    for l in lines:
        out.append(list(map(int, list(l.strip()))))
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    res = parse(lines)
    print(res)
    print(p11_1(res))
    res = parse(lines)
    print(p11_2(res))
    f.close()

