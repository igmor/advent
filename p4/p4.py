import argparse
from collections import defaultdict

def most_least_common_bits(l: list[str]) -> dict[list[int]]:
    ml_bits = defaultdict(lambda : [0, 0])
    for n in l:
        i = 0
        print(n)
        for c in n:
            if c == "0":
                ml_bits[i][0] += 1
            elif c == "1":
                ml_bits[i][1] += 1
            i += 1
    return ml_bits

def p4_1(l: list[str]):
    ml_bits = most_least_common_bits(l)
    gamma = ""
    epsilon = ""
    for i in range(len(l[0])-1):
        if ml_bits[i][0] > ml_bits[i][1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    print(gamma, epsilon)
    return int(gamma,2) * int(epsilon, 2)

def filter(l: list[str], current: int, ml_bits:dict[list[int]], oxigen: int):
    out = list[str]()
    print(ml_bits[current])
    for n in l:
        if ml_bits[current][0] > ml_bits[current][1]:
            if oxigen == '1':
                if n[current] == '0':
                    out.append(n)
            else:
                if n[current] == '1':
                    out.append(n) 
        elif ml_bits[current][0] < ml_bits[current][1]:
            if oxigen == '1':
                if n[current] == '1':
                    out.append(n)
            else:
                if n[current] == '0':
                    out.append(n) 
        else:
            if n[current] == oxigen:
                out.append(n)

    if not out:
        return [l[0]]

    return out

def p4_2(l: list[str]):
    ml_bits = most_least_common_bits(l)
    gamma = ""
    epsilon = ""
    ws = l
    oxigen = None
    for i in range(len(l[0])-1):
        print(ws)
        if len(ws) == 1:
            oxigen = ws[0]
            break
        ws = filter(ws, i, ml_bits, '1')
        ml_bits = most_least_common_bits(ws)

    if not oxigen:
        oxigen = ws[0]
    ws = l
    co2_scrubber = None
    for i in range(len(l[0])-1):
        print(ws)
        if len(ws) == 1:
            co2_scrubber = ws[0]
            break
        ws = filter(ws, i, ml_bits, '0')
        ml_bits = most_least_common_bits(ws)

    if not co2_scrubber:
        co2_scrubber = ws[0]

    print(oxigen, co2_scrubber)
    return int(oxigen,2) * int(co2_scrubber, 2)

def parse(lines: list[str]) -> list[str]:
    out = list[str]()
    for l in lines:
        out.append(l)
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    digits = parse(lines)
    #print(digits)
    print(p4_1(digits))
    print(p4_2(digits))
    f.close()

