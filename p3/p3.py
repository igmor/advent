import argparse

def p3(l: list[tuple[str, int]]):
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
    print(p3(pos))
    f.close()

