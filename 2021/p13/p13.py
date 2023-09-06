import argparse
from collections import defaultdict

def traverse(caves: dict[str,list[str]], visited: dict[str, bool], path: list[str], valid_pathes: list[list[str]], n):
    print(path)
    current = path[-1]
    if current.islower() and visited[current] >= n:
        return
    visited[current] += 1
    for t in caves[current]:
        if t == "end":
            valid_pathes.append(path + [t])
        else:
            traverse(caves, visited, path + [t], valid_pathes, n)
    visited[current] -= 1

def traverse2(caves: dict[str,list[str]], visitedSingle: bool, visited: dict[str, bool], path: list[str], valid_pathes: list[list[str]], n):
    print(path)
    current = path[-1]
    if current.islower() and visited[current] >= n:
        return
    visited[current] += 1
    if current.islower():
        if visited[current] == 2: 
            if not visitedSingle: 
                visitedSingle = True
            else:
                visited[current] -= 1
                return
            
    for t in caves[current]:
        if t == "end":
            valid_pathes.append(path + [t])
        else:
            traverse2(caves, visitedSingle, visited, path + [t], valid_pathes, n)
    if current.islower() and visited[current] == 2 and visitedSingle:
        visitedSingle = False
    visited[current] -= 1

def p12_1(caves: dict[str,list[str]]):
    pathes = []
    visited = dict[str, int]()
    for v in caves.keys():
        visited[v] = 0

    start = ['start']
    valid_pathes = []
    traverse(caves, visited, start, valid_pathes, 1)
    print("valid paths")
    print("________________________________________")

    for p in valid_pathes:
        print(','.join(p))
    return len(valid_pathes)

def p12_2(caves: dict[str,list[str]]):
    pathes = []
    visited = dict[str, int]()
    for v in caves.keys():
        visited[v] = 0

    start = ['start']
    valid_pathes = []
    visitedSingle = False
    traverse2(caves, visitedSingle, visited, start, valid_pathes, 2)
    print("valid paths")
    print("________________________________________")

    for p in valid_pathes:
        print(','.join(p))
    return len(valid_pathes)

def parse(lines: list[str]) -> dict[str,list[str]]:
    caves = defaultdict(set)
    for l in lines:
        s, t = l.strip().split('-')
        if t != 'start':
            caves[s].add(t)
        if s != 'start':
            caves[t].add(s)
    return caves

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    res = parse(lines)
    print(res)
#    print(p12_1(res))
    res = parse(lines)
    print(p12_2(res))
    f.close()

