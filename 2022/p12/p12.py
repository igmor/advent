from typing import List, Tuple, Callable
import argparse
import sys

def height(hm: List[List[str]], i,j: int) -> int:
    if hm[i][j] == 'S':
        return 0
    if hm[i][j] == 'E':
        return ord('z') - ord('a')
    
    return ord(hm[i][j]) - ord('a')

import heapq

def p11(hm: List[List[str]], visited: List[List[int]], start: List[int], end: List[int], path: List[List[int]]) -> int:
    # Initialize the distance and visited arrays
    dist = [[float('inf') for j in range(len(hm[0]))] for i in range(len(hm))]
    dist[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 1

    # Initialize the priority queue with the start node
    pq = [(0, start)]

    while pq:
        # Get the node with the smallest distance from the start
        cur_dist, cur = heapq.heappop(pq)

        # If we've reached the end node, return the distance
        if cur == end:
            return cur_dist

        # Check the neighbors of the current node
        for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nexti = cur[0] + i
            nextj = cur[1] + j

            # Check if the neighbor is within the bounds of the grid
            if nexti >= 0 and nexti < len(hm) and nextj >= 0 and nextj < len(hm[0]):
                # Calculate the height difference between the current node and the neighbor
                h1 = height(hm, cur[0], cur[1])
                h2 = height(hm, nexti, nextj)
                diff = h2 - h1

                # Check if the neighbor is reachable and has a shorter distance from the start
                if diff <= 1 and visited[nexti][nextj] == 0 and cur_dist + 1 < dist[nexti][nextj]:
                    visited[nexti][nextj] = 1
                    dist[nexti][nextj] = cur_dist + 1
                    heapq.heappush(pq, (dist[nexti][nextj], [nexti, nextj]))

    # If we've exhausted all nodes and haven't reached the end, return -1
    return -1

    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    f = open(args.input, 'r')
    lines = f.readlines()
    f.close()
    hm = []
    for l in lines:
        l = l.replace('\n', '')
        if not l:
            continue
        hm.append(list(l))
    start = []
    end = []
    for i in range(len(hm)):
        for j in range(len(hm[0])):
            if hm[i][j] == 'S':
                start = [i, j]
            if hm[i][j] == 'E':
                end = [i, j]
            
    visited = [[0 for j in range(len(hm[0]))] for i in range(len(hm))]
    path = []
    visited[start[0]][start[1]] = 1
    print(p11(hm, visited, start, end, path))

    starts = []
    end = []
    for i in range(len(hm)):
        for j in range(len(hm[0])):
            if hm[i][j] == 'S' or hm[i][j] == 'a':
                starts.append([i, j])
            if hm[i][j] == 'E':
                end = [i, j]

    min_dist = float('inf')
    print(starts)
    for s in starts:
        visited = [[0 for j in range(len(hm[0]))] for i in range(len(hm))]
        path = []
        visited[s[0]][s[1]] = 1

        dist = p11(hm, visited, s, end, path)
        print(dist)
        if dist < min_dist and dist != -1:
            min_dist = dist
    print(min_dist)