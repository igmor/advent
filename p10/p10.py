import argparse
from collections import defaultdict

Area = list[list[int]]
Basins = list[set[int]]

def p9_1(area: Area, n:int):
    s = 0
    for i in range(1, len(area)-1):
        for j in range(1, n+1):
            if area[i][j] < area[i-1][j] and area[i][j] < area[i+1][j] and area[i][j] < area[i][j-1] and area[i][j] < area[i][j+1]:
                s += (1 + area[i][j])
    return s

def search_basins(area, visited: Area, n:int, i, j: int, basins, current_basin):
    visited[i][j] = 1
    current_basin.append(area[i][j])
    if i > 1 and area[i-1][j] != 9 and visited[i-1][j] == 0:
        search_basins(area, visited, n, i-1, j, basins, current_basin)
    if i < n+2 and area[i+1][j] != 9 and visited[i+1][j] == 0:
        search_basins(area, visited, n, i+1, j, basins, current_basin)
    if j > 1 and area[i][j-1] != 9 and visited[i][j-1] == 0:
        search_basins(area, visited, n, i, j-1, basins, current_basin)
    if j < n+2 and area[i][j+1] != 9 and visited[i][j+1] == 0:
        search_basins(area, visited, n, i, j+1, basins, current_basin)

def p9_2(area: Area, n:int):
    visited = [[0 for x in range(n+2)] for y in range(n+2)] 
    print(visited)
    basins = Basins()
    current_basin = list[int]()
    for i in range(1, len(area)-1):
        for j in range(1, n+1):
            if area[i][j] != 9 and visited[i][j] == 0:
                search_basins(area, visited, n, i, j, basins, current_basin)
                basins.append(current_basin)
                current_basin = list[int]()

    if current_basin:
        basins.append(current_basin)
    basins = sorted(basins, key = lambda x: len(x))
    print(basins)
    return len(basins[-1]) * len(basins[-2]) * len(basins[-3])

def parse(lines: list[str]) -> (Area, int):
    area = Area()
    n = 0
    for l in lines:
        new_row = [9]
        row = list(map(lambda x: int(x.strip()), list(l.strip('\n'))))
        n = len(row)
        if not area:
            area.append((n+2)*[9])
        new_row.extend(row)
        new_row.append(9)
        area.append(new_row)
    area.append((n+2)*[9])
    return area, n

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    res, n = parse(lines)
    print(res)
    print(p9_1(res, n))
    seq = parse(lines)
    print(p9_2(res, n))
    f.close()

