from typing import List
import argparse

def num_row_visible(grid: List[List[str]], ifrom, ito, jfrom, jto: int, visible: List[List[int]]) -> int:
    total = 0

    for i in range(ifrom if ifrom < ito else ifrom-1, ito if ifrom < ito else ito - 1, 1 if ifrom < ito else -1):
        tallest = -1
        for j in range(jfrom if jfrom < jto else jfrom-1, jto if jfrom < jto else jto - 1, 1 if jfrom < jto else -1):
            if int(grid[i][j]) > tallest:
                tallest = int(grid[i][j])
                visible[i][j] = 1
        #print(tallest)

def num_col_visible(grid: List[List[str]], ifrom, ito, jfrom, jto: int, visible: List[List[int]]) -> int:
    total = 0

    for i in range(ifrom if ifrom < ito else ifrom-1, ito if ifrom < ito else ito - 1, 1 if ifrom < ito else -1):
        tallest = -1
        for j in range(jfrom if jfrom < jto else jfrom-1, jto if jfrom < jto else jto - 1, 1 if jfrom < jto else -1):
            if int(grid[j][i]) > tallest:
                tallest = int(grid[j][i])
                visible[j][i] = 1
        #print(tallest)

def num_row_score(grid: List[List[str]], ifrom, ito, jfrom, jto: int, visible: List[List[int]], score: List[List[List[int]]]) -> int:
    total = 0

    score_index = 0 if ifrom < ito else 1

    for i in range(ifrom if ifrom < ito else ifrom-1, ito if ifrom < ito else ito - 1, 1 if ifrom < ito else -1):
        score_vis = 0
        tallestj = 0 if jfrom < jto else jfrom-1
        tallest = -1

        for j in range(jfrom if jfrom < jto else jfrom-1, jto if jfrom < jto else jto - 1, 1 if jfrom < jto else -1):
            score[i][j][score_index] = score_vis
            if int(grid[i][j]) < tallest:
                score[i][j][score_index] = max(j, tallestj) - min(j, tallestj)
                continue
            else:
                tallest = int(grid[i][j])
                score[i][j][score_index] = max(j, tallestj) - min(j, tallestj)
                talletsj = j

        #print(tallest)

def num_col_score(grid: List[List[str]], ifrom, ito, jfrom, jto: int, visible: List[List[int]], score: List[List[List[int]]]) -> int:
    total = 0

    score_index = 2 if ifrom < ito else 3
    for i in range(ifrom if ifrom < ito else ifrom-1, ito if ifrom < ito else ito - 1, 1 if ifrom < ito else -1):
        score_vis = 0
        tallestj = 0 if jfrom < jto else jfrom-1
        tallest = -1

        for j in range(jfrom if jfrom < jto else jfrom-1, jto if jfrom < jto else jto - 1, 1 if jfrom < jto else -1):
            if int(grid[j][i]) < tallest:
                score[j][i][score_index] = max(j, tallestj) - min(j, tallestj)
                continue
            else:
                tallest = int(grid[j][i])
                score[j][i][score_index] = max(j, tallestj) - min(j, tallestj)
                tallestj = j

        #print(tallest)

def p11(grid: List[List[str]]) -> (int, List[List[int]]):
    total = 0
    visible = [[0 for col in range(len(grid))] for row in range(len(grid))]

    num_row_visible(grid, 0, len(grid), 0, len(grid[0]), visible)
    num_row_visible(grid, len(grid), 0, len(grid[0]), 0, visible)
    num_col_visible(grid, 0, len(grid), 0, len(grid[0]), visible)
    num_col_visible(grid, len(grid), 0, len(grid[0]), 0, visible)
    total = sum(sum(x) for x in visible)
    #print(visible)

    return total, visible

def p21(grid: List[List[str]], visible: List[List[int]]) -> int:
    score = [[[0, 0, 0, 0] for col in range(len(grid))] for row in range(len(grid))]

 #   num_row_score(grid, 0, len(grid), 0, len(grid[0]), visible, score)
 #   num_row_score(grid, len(grid), 0, len(grid[0]), 0, visible, score)
 #   num_col_score(grid, 0, len(grid), 0, len(grid[0]), visible, score)
 #   num_col_score(grid, len(grid), 0, len(grid[0]), 0, visible, score)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            tallest = int(grid[i][j])
            j1 = j + 1
            while j1 < len(grid[0]) and int(grid[i][j1]) <= tallest:
                score[i][j][1] +=1
                if int(grid[i][j1]) == tallest:
                    break
                j1 += 1
            if j1 < len(grid[0]) and int(grid[i][j1]) > tallest:
                score[i][j][1] +=1
            j1 = j - 1
            while j1 >= 0 and int(grid[i][j1]) <= tallest:
                score[i][j][0] +=1
                if int(grid[i][j1]) == tallest:
                    break
                j1 -= 1
            if j1 >= 0 and int(grid[i][j1]) > tallest:
                score[i][j][1] +=1                
            i1 = i + 1
            while i1 < len(grid) and int(grid[i1][j]) <= tallest:
                score[i][j][3] += 1
                if int(grid[i1][j]) == tallest:
                    break
                i1 += 1
            if i1 < len(grid) and int(grid[i1][j]) > tallest:
                score[i][j][1] +=1                
            i1 = i - 1
            while i1 >= 0 and int(grid[i1][j]) <= tallest:
                score[i][j][2] += 1
                if int(grid[i1][j]) == tallest:
                    break
                i1 -= 1
            if i1 >= 0 and int(grid[i1][j]) > tallest:
                score[i][j][1] +=1                

    print(score)
    m_visible = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s = score[i][j][0]*score[i][j][1]*score[i][j][2]*score[i][j][3]
            if s > m_visible:
                m_visible = s
    return m_visible

def print_pr(something: List[List[List[int]]]):
    for i in range(len(grid)):
        print(grid[i])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    grid = []
    for l in lines:
        l = l.replace('\n', '')
        grid.append(list(l))
    total, visible = p11(grid)
    print(visible)
    print(total)
    print(p21(grid, visible))


