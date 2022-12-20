#! /usr/bin/env python3
import sys
import re

YLINE = 4000000
YMIN  = 0 

def merge(y, S):
    m = []
    for s in S:
        if len(m) == 0:
            m = s
        else:
            if m[-1] >= s[0]-1 and m[-1] <= s[-1]:
                m = [m[0], s[-1]]
            elif not m[-1] >= s[-1]:
                print(4000000*abs(s[0]-1) + y)
                exit(0)

    #print("after", m)

def main():
    # [sensorx, sensory, beaconx, beacony]
    coords = []

    # read input
    while (line:=sys.stdin.readline()):
         coords.append(tuple(map(int, re.findall(r'([-0-9]+)', line))))

    for yline in range(YMIN, YLINE):
        print(yline)
        S = []
        for sx, sy, bx, by in coords:       
            dist = abs(bx-sx) + abs(by-sy)
            distToLine = abs(yline-sy)
            if distToLine <= dist:
                r = dist - distToLine
                S.append([sx-r, sx+r])

        S.sort(key=lambda x:x[0])
        #print("before", S)
        merge(yline, S)

if __name__ == "__main__":
    main()
