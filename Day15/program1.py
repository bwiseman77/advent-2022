#! /usr/bin/env python3
import sys
import re

YLINE = 2000000

def main():
    # [sensorx, sensory, beaconx, beacony]
    coords = []

    # read input
    while (line:=sys.stdin.readline()):
         coords.append(tuple(map(int, re.findall(r'([-0-9]+)', line))))

    S = set()
    NumB = 0
    for sx, sy, bx, by in coords:      
        if by == YLINE:
            if bx not in S:
                S.add(bx)
                NumB += 1

        dist = abs(bx-sx) + abs(by-sy)
        distToLine = abs(YLINE-sy)
        if distToLine <= dist:
            for i in range(0, dist-distToLine+1):
                S.add(sx+i)
                S.add(sx-i)

    print(len(S) - NumB)
    #print(NumB)
    #print(S)

if __name__ == "__main__":
    main()
