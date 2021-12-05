import argparse
from collections import defaultdict

Point = tuple[int, int]
Segment = tuple[Point, Point]

def p6_1(max_point: Point, l: list[Segment]) -> int:
    m_overlap = 0
    field = [[0 for x in range(max_point[0]+1)] for y in range(max_point[1]+1)]
    #print(field)
    for s in l:
        if s[0][0] == s[1][0]:
            #print(s)
            for i in range(min(s[0][1], s[1][1]), max(s[0][1], s[1][1])+1):
                field[s[0][0]][i] += 1
        if s[0][1] == s[1][1]:
            #print(s)
            for i in range(min(s[0][0], s[1][0]), max(s[0][0], s[1][0])+1):
                field[i][s[0][1]] += 1

    for i in range(max_point[0]+1):
        for j in range(max_point[1]+1):
            if field[i][j] > 1:
                m_overlap += 1
    #print(field)
    return m_overlap

def p6_2(max_point: Point, l: list[Segment]) -> int:
    m_overlap = 0
    field = [[0 for x in range(max_point[0]+1)] for y in range(max_point[1]+1)]
    #print(field)
    for s in l:
        if s[0][0] == s[1][0]:
            #print(s)
            for i in range(min(s[0][1], s[1][1]), max(s[0][1], s[1][1])+1):
                field[s[0][0]][i] += 1
        if s[0][1] == s[1][1]:
            #print(s)
            for i in range(min(s[0][0], s[1][0]), max(s[0][0], s[1][0])+1):
                field[i][s[0][1]] += 1
        if abs(s[0][0] - s[1][0]) == abs(s[0][1] - s[1][1]):
            dir_x = 1 if s[0][0] < s[1][0] else -1
            dir_y = 1 if s[0][1] < s[1][1] else -1

            x = s[0][0]
            y = s[0][1]
            while x != s[1][0] or y != s[1][1]:
                field[x][y] += 1
                x += dir_x
                y += dir_y
            field[x][y] += 1

    for i in range(max_point[0]+1):
        for j in range(max_point[1]+1):
            if field[i][j] > 1:
                m_overlap += 1
    #print(field)
    return m_overlap

def parse(lines: list[str]) -> tuple[Point, list[Segment]]:
    out = list[Segment]()
    m_x = 0
    m_y = 0
    for l in lines:
        p1, p2 = l.split("->")
        p1_x, p1_y = p1.split(',')
        p2_x, p2_y = p2.split(',')

        p1_x = int(p1_x.strip())
        p1_y = int(p1_y.strip())
        p2_x = int(p2_x.strip())
        p2_y = int(p2_y.strip())

        if p1_x > m_x:
            m_x = p1_x
        if p2_x > m_x:
            m_x = p2_x
        if p1_y > m_y:
            m_y = p1_y
        if p2_y > m_y:
            m_y = p2_y

        out.append(
            Segment((Point((p1_x, p1_y)), Point((p2_x, p2_y))))
        )
    return Point((m_x, m_y)), out

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="count the number of increased after decreased depths")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    max_point, segments = parse(lines)
    #print(max_point, segments)
    print(p6_1(max_point, segments))
    print(p6_2(max_point, segments))

    f.close()

