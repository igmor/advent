from typing import Dict, List, Tuple, Callable
import argparse
import sys
import ast
import functools
import copy

from collections import defaultdict

def p11(result: List[Tuple[int, int, int]]) -> int:
    xy = defaultdict(int)
    yz = defaultdict(int)
    xz = defaultdict(int)

    for c in result:
        x = c[0]
        y = c[1]
        z = c[2]

        xy[(x, y, z)] += 1
        xy[(x, y, z+1)] += 1

        yz[(y, z, x)] += 1
        yz[(y, z, x+1)] += 1

        xz[(x, z, y)] += 1
        xz[(x, z, y+1)] += 1

    total = 0
    for k, v in xy.items():
        if v == 1:
            total += 1

    for k, v in yz.items():
        if v == 1:
            total += 1

    for k, v in xz.items():
        if v == 1:
            total += 1

    return total


def p12(result: List[str]) -> int:
    xy = defaultdict(int)
    yz = defaultdict(int)
    xz = defaultdict(int)

    for c in result:
        x = c[0]
        y = c[1]
        z = c[2]

        xy[(x, y, z)] += 1
        xy[(x, y, z+1)] += 1

        yz[(y, z, x)] += 1
        yz[(y, z, x+1)] += 1

        xz[(x, z, y)] += 1
        xz[(x, z, y+1)] += 1

    faces = []

    out = []
    current = []

    visited = {}
    for c in result:
        print(c)
        x0, y0, z0 = c
        if xy[(x0, y0, z0)] < 2:
            faces.append((0, (x0, y0, z0)))

        while faces:
            plane, face = faces.pop()

            if (plane, face) in visited:
                continue
            
            x, y, z = face
            visited[(plane, face)] = True

            current.append((plane, face))

            #xy plane

            if plane == 0:
                down0 = (0, (x, y-1, z))
                if down0[1] in xy and xy[down0[1]] == 1:
                    faces.append((0, down0[1]))
                top0 = (0, (x, y+1, z))
                if top0[1] in xy and xy[top0[1]] == 1:
                    faces.append((0, top0[1]))  
                left0 = (0, (x-1, y, z))
                if left0[1] in xy and xy[left0[1]] == 1:
                    faces.append((0, left0[1]))
                right0 = (0, (x+1, y, z))
                if right0[1] in xy and xy[right0[1]] == 1:
                    faces.append((0, right0[1]))

                down0 = (1, (y, z, x))
                if down0[1] in yz and yz[down0[1]] == 1:
                    faces.append((1, down0[1]))
                top0 = (1, (y, z-1, x))
                if top0[1] in yz and yz[top0[1]] == 1:
                    faces.append((1, top0[1]))  

                down0 = (1, (y, z, x+1))
                if down0[1] in yz and yz[down0[1]] == 1:
                    faces.append((1, down0[1]))
                top0 = (1, (y, z-1, x+1))
                if top0[1] in yz and yz[top0[1]] == 1:
                    faces.append((1, top0[1]))  

                down0 = (2, (x, z, y))
                if down0[1] in xz and xz[down0[1]] == 1:
                    faces.append((2, down0[1]))
                top0 = (2, (x, z-1, y))
                if top0[1] in xz and xz[top0[1]] == 1:
                    faces.append((2, top0[1]))  

                down0 = (2, (x+1, z, y))
                if down0[1] in xz and xz[down0[1]] == 1:
                    faces.append((2, down0[1]))
                top0 = (2, (x+1, z-1, y))
                if top0[1] in xz and xz[top0[1]] == 1:
                    faces.append((2, top0[1]))  

            if plane == 1:
                y, z, x = x, y, z
                down0 = (1, (y-1, z, x))
                if down0[1] in yz and yz[down0[1]] == 1:
                    faces.append((1, down0[1]))
                top0 = (1, (y+1, z, x))
                if top0[1] in yz and yz[top0[1]] == 1:
                    faces.append((1, top0[1]))  
                left0 = (1, (y, z+1, x))
                if left0[1] in yz and yz[left0[1]] == 1:
                    faces.append((1, left0[1]))
                right0 = (1, (y, z-1, x))
                if right0[1] in yz and yz[right0[1]] == 1:
                    faces.append((1, right0[1]))

                down0 = (0, (x, y, z))
                if down0[1] in xy and xy[down0[1]] == 1:
                    faces.append((0, down0[1]))
                top0 = (0, (x-1, y, z))
                if top0[1] in xy and xy[top0[1]] == 1:
                    faces.append((0, top0[1]))  

                down0 = (0, (x, y, z+1))
                if down0[1] in xy and xy[down0[1]] == 1:
                    faces.append((0, down0[1]))
                top0 = (0, (x-1, y, z+1))
                if top0[1] in xy and xy[top0[1]] == 1:
                    faces.append((0, top0[1]))  

                down0 = (2, (x, z, y))
                if down0[1] in xz and xz[down0[1]] == 1:
                    faces.append((2, down0[1]))
                top0 = (0, (x-1, z, y))
                if top0[1] in xz and xz[top0[1]] == 1:
                    faces.append((2, top0[1]))  

                down0 = (2, (x, z, y+1))
                if down0[1] in xz and xz[down0[1]] == 1:
                    faces.append((2, down0[1]))
                top0 = (0, (x-1, z, y+1))
                if top0[1] in xz and xz[top0[1]] == 1:
                    faces.append((2, top0[1]))  

            if plane == 2:
                x, z, y = x, y, z
                down0 = (2, (x, z-1, y))
                if down0[1] in xz and xz[down0[1]] == 1:
                    faces.append((2, down0[1]))
                top0 = (2, (x, z+1, y))
                if top0[1] in xz and xz[top0[1]] == 1:
                    faces.append((2, top0[1]))  
                left0 = (2, (x-1, z, y))
                if left0[1] in xz and xz[left0[1]] == 1:
                    faces.append((2, left0[1]))
                right0 = (2, (x+1, z, y))
                if right0[1] in xz and xz[right0[1]] == 1:
                    faces.append((2, right0[1]))

                # down0 = (0, (x, y, z))
                # if down0[1] in xy and xy[down0[1]] == 1:
                #     faces.append((0, down0[1]))
                # top0 = (0, (x, y-1, z))
                # if top0[1] in xy and xy[top0[1]] == 1:
                #     faces.append((0, top0[1]))  

                # down0 = (0, (x, y, z+1))
                # if down0[1] in xy and xy[down0[1]] == 1:
                #     faces.append((0, down0[1]))
                # top0 = (0, (x, y-1, z+1))
                # if top0[1] in xy and xy[top0[1]] == 1:
                #     faces.append((0, top0[1]))  

        if current:
            out.append(current)
        current = []

    for c in out:
        print(c, len(c))

    for xx in xy:
        if (0, xx) not in visited:
            print('not visited', xx, xy[xx])
    for yy in yz:
        if (1, yy) not in visited:
            print('not visited', yy, yz[yy])
    for zz in xz:
        if (2, zz) not in visited:
            print('not visited', zz, xz[zz])

    return 0

def visit_faces(faces: List[Tuple[int, Tuple[int, int, int]]], visited: Dict[Tuple[int, Tuple[int, int, int]], bool], out: List[Tuple[int, int, int]]):
        while faces:
            plane, face = faces.pop()

            if (plane, face) in visited:
                continue
            
            x, y, z = face
            visited[(plane, face)] = True
            current.append((x, y, z))

            #xy plane

            if plane == 0:
                down0 = (0, (x, y-1, z))
                if down0[1] in xy and xy[down0[1]] == 1:
                    faces.append(down0)
                top0 = (0, (x, y+1, z))
                if top0[1] in xy and xy[top0[1]] == 1:
                    faces.append(top0)            
                left0 = (0, (x-1, y, z))
                if left0[1] in xy and xy[left0[1]] == 1:
                    faces.append(left0)
                right0 = (0, (x+1, y, z))
                if right0[1] in xy and xy[right0[1]] == 1:
                    faces.append(right0)

            #yz plane
            if plane == 0:
                down1 = (1, (x, y-1, z))
                if down1[1] in yz and yz[down1[1]] == 1:
                    faces.append(down1)
                top1 = (1, (x, y+1, z))
                if top1[1] in yz and yz[top1[1]] == 1:
                    faces.append(top1)
                left1 = (1, (x, y, z-1))
                if left1[1] in yz and yz[left1[1]] == 1:
                    faces.append(left1)
                right1 = (1, (1, (x, y, z+1)))
                if right1[1] in yz and yz[right1[1]] == 1:
                    faces.append(right1)

            #xz plane
            if plane == 2:
                down2 = (2, (x-1, y, z))
                if down2[1] in xz and xz[down2[1]] == 1:
                    faces.append(down2)
                top2 = (2, (x+1, y, z))
                if top2[1] in xz and xz[top2[1]] == 1:
                    faces.append(top2)
                left2 = (2, (x, y, z-1))
                if left2[1] in xz and xz[left2[1]] == 1:
                    faces.append(left2)
                right2 = (2, (x, y, z+1))
                if right2[1] in xz and xz[right2[1]] == 1:
                    faces.append(right2)

        if current:
            out.append(current)
        current = []


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input file")
    args = parser.parse_args()

    result = []
    f = open(args.input, 'r')
    lines = f.readlines()
    for l in lines:
        l = l.replace('\n','')
        x, y, z = l.split(',')
        x = int(x)
        y = int(y)
        z = int(z)

        result.append((x, y, z))
    #print(result)

    print(p11(result))
    print(p12(result))
