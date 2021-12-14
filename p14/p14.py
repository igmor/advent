import argparse
from collections import defaultdict

Paper = list[list[int]]
Folds = list[tuple[int, int]]

def p14_1(paper: Paper, folds: Folds) -> int:
    n  = 0
    fold = folds[0]
    print(fold)
    for i in range(len(paper)):
        for j in range(len(paper[0])):
            if paper[i][j] == 1:
                n += 1
            if fold[0] == 1:
                fy = fold[1]
                if i > fy:
                    print(paper[2*fy-i][j])
                    if paper[i][j] == 1 and paper[2*fy-i][j] == 1:
                        n -= 1
                        print("move: ", (i, j), (2*fy-i, j))
                    paper[2*fy-i][j] = paper[i][j] or paper[2*fy-i][j]

            if fold[0] == 0:
                fx = fold[1]
                if j > fx:
                    if paper[i][j] == 1 and paper[i][2*fx-j] == 1:
                        n -= 1
                        print("move: ", (i, j), (i, 2*fx - j))

                    paper[i][2*fx-j] = paper[i][j] or paper[i][2*fx-j]

    for l in paper:
        print(l)
    return n

def p14_2(paper: Paper, folds: Folds) -> int:
    n  = 0
    for fold in folds:
        for i in range(len(paper)):
            for j in range(len(paper[0])):
                if paper[i][j] == 1:
                    n += 1
                if fold[0] == 1:
                    fy = fold[1]
                    if i > fy:
                        if paper[i][j] == 1 and paper[2*fy-i][j] == 1:
                            n -= 1
                        paper[2*fy-i][j] = paper[i][j] or paper[2*fy-i][j]

                if fold[0] == 0:
                    fx = fold[1]
                    if j > fx:
                        if paper[i][j] == 1 and paper[i][2*fx-j] == 1:
                            n -= 1
                        paper[i][2*fx-j] = paper[i][j] or paper[i][2*fx-j]

    return n


def parse(lines: list[str]) -> (Paper, Folds):
    out = list[tuple[int, int]]()

    folds = Folds()
    maxx = -1
    maxy = -1
    for l in lines:
        pair = l.strip().split(',')
        if len(pair) == 2:
            pair = list(map(int, l.strip().split(',')))
            if pair[0] > maxx:
                maxx = pair[0]
            if pair[1] > maxy:
                maxy = pair[1]
            out.append(pair)
        if l.startswith("fold"):
            f, a, eq = l.strip().split()
            dim, n = eq.split('=')
            folds.append((0 if dim == 'x' else 1, int(n)))

    paper = [[0 for x in range(maxx+1)] for y in range(maxy+1)]

    for o in out:
        paper[o[1]][o[0]] = 1
    return paper, folds

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    paper, folds = parse(lines)
 #   print(paper, folds)
    print(p14_1(paper, folds))
    paper, folds = parse(lines)
    print(p14_2(paper, folds))
    fout = open("out.txt", 'w')
    for p in paper:
        for c in p:
            if c == 0:
                fout.write('.')
            else:
                fout.write('#')
        fout.write('\n')
    fout.close()
    f.close()

