import argparse
from collections import defaultdict

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def p10_1(lines: list[list[int]]):
    s = 0
    n = 0
    for l in lines:
        s = []
        for c in l:
            if c in ['(', '[', '{', '<']:
                s.append(c)
            else:
                if len(s) == 0:
                    n += scores[c]
                    break
                if c == ')' and s[-1] == '(':
                    s.pop()
                elif c == ']' and s[-1] == '[':
                    s.pop()
                elif c == '}' and s[-1] == '{':
                    s.pop()
                elif c == '>' and s[-1] == '<':
                    s.pop()
                else:
                    n += scores[c]
                    break
    return n

p2_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

auto_d = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
def score(line: list[int]) -> int:
    s = 0
    for c in line:
        s = 5*s + p2_scores[c]
    return s

def p10_2(lines: list[list[int]]):
    s = 0
    scores = []
    for l in lines:
        s = []
        auto_complete = True
        for c in l:
            if c in ['(', '[', '{', '<']:
                s.append(c)
            else:
                if len(s) == 0:
                    auto_complete = False
                    break
                if c == ')' and s[-1] == '(':
                    s.pop()
                elif c == ']' and s[-1] == '[':
                    s.pop()
                elif c == '}' and s[-1] == '{':
                    s.pop()
                elif c == '>' and s[-1] == '<':
                    s.pop()
                else:
                    auto_complete = False
                    break
        # now the real business
        if auto_complete:
            auto_c_line = list[int]()
            while s:
                auto_c_line.append(auto_d[s.pop()])
            scores.append(score(auto_c_line))
    scores = sorted(scores)
    print(scores)
    return scores[int(len(scores)/2)]

def parse(lines: list[str]) -> list[list[int]]:
    out = []
    for l in lines:
        out.append(list(l.strip()))
    return out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    res = parse(lines)
    print(res)
    print(p10_1(res))
    res = parse(lines)
    print(p10_2(res))
    f.close()

