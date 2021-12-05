import argparse

def p3_1(l: list[tuple[str, int]]):
    x = 0
    d = 0
    for (direction, by) in l:
        if direction == "forward":
            x += by
        if direction == "up":
            d -= by
        if direction == "down":
            d += by
    return x * d

def p3_2(l: list[tuple[str, int]]):
    x = 0
    d = 0
    aim = 0
    for (direction, by) in l:
        if direction == "forward":
            d += aim * by
            x += by
        if direction == "up":
            aim -= by
        if direction == "down":
            aim += by
    print(aim, d, x)
    return x * d

def parse(lines: list[str]) -> list[tuple[str, int]]:
    out = list[tuple[str, int]]()
    for l in lines:
        direction, by = l.split()
        out.append((direction, int(by)))
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    pos = parse(lines)
    print(pos)
    print(p3_1(pos))
    print(p3_2(pos))
    f.close()

