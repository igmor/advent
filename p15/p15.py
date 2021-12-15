import argparse
from collections import defaultdict

Pairs = dict[str, str]

def p14_1(pairs: Pairs, seq: str, n:int) -> int:

    step = seq
    res = ""
    prev = -1
    d = defaultdict(int)
    for c in step:
        d[c] += 1

    for i in range(n):
        print(i, step)
        for i in range(1, len(step)):
            #print(step[i-1:i+1], pairs[step[i-1:i+1]])
            if pairs.get(step[i-1:i+1]):
                d[pairs[step[i-1:i+1]]] += 1
                res += (step[i-1] if prev != i-1 else "") + pairs[step[i-1:i+1]] + step[i]
                prev = i
        step = res
        res = ""

    out = sorted(d.values())

    return out[-1] - out[0]

def p14_2(pairs: Pairs, seq: str, n:int) -> int:
    d = defaultdict(int)
    for c in seq:
        d[c] += 1
    dd = defaultdict(int)
    for i in range(1, len(seq)):
        dd[seq[i-1:i+1]] += 1

    print(dd)

    for i in range(n):
        d_perm = defaultdict(int)
        for p in dd.keys():
            if pairs.get(p) and dd[p] > 0:
                print(p, p[0]+pairs[p], pairs[p]+p[1])
                d_perm[p[0]+pairs[p]] += dd[p]
                d_perm[pairs[p]+p[1]] += dd[p]
                d[pairs[p]] += dd[p]
                dd[p] = 0
        for k in d_perm.keys():
            dd[k] += d_perm[k]
        print(dd, i)

    out = sorted(d.values())
    print(d)

    return out[-1] - out[0]

def parse(lines: list[str]) -> tuple[Pairs, str]:
    out = Pairs()
    seq = lines[0].strip()

    for l in lines[2:]:
        pair = l.strip().split('->')
        if len(pair) == 2:
            out[pair[0].strip()] =  pair[1].strip()
    return out, seq

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    pairs, seq = parse(lines)
    print(pairs, seq)
    print(p14_1(pairs, seq, 10))
    pairs, seq = parse(lines)
    print(p14_2(pairs, seq, 40))
    f.close()

