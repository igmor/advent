import argparse
from collections import defaultdict

def p7_1(seq: list[int], ngen):
    for i in range(ngen):
        new_fish = []
        for j in range(len(seq)):
            if seq[j] == 0:
                new_fish.append(8)
                seq[j] = 6
            else:
                seq[j] -= 1
        seq.extend(new_fish)
    return len(seq)

def p7_2(seq: list[int], ngen):
    print(seq)
    d = defaultdict(int)
    for v in seq:
        d[v] += 1
    print(d)
    for j in range(ngen):
        d_newgen = defaultdict(int)
        for i in range(8, -1, -1):
            if i > 0:
                d_newgen[i-1] = d[i]
            else:
                d_newgen[8] = d[i]
                d_newgen[6] += d[i]
        d = d_newgen
        print(d_newgen)
    tot = 0
    for k, v in d.items():
        tot += v

    return tot

def parse(lines: list[str]):
    return list(map(lambda x: int(x), lines[0].strip().split(',')))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    seq = parse(lines)
    print(p7_1(seq, 80))
    seq = parse(lines)
    print(p7_2(seq, 256))
    f.close()

