#! /usr/bin/env python3
import sys

SIZE  = 1000#30
XOFF  = 0#490
YOFF  = 0
DROP  = 500
MAX   = 0

def add_lines(grid, points):
    for line in points:
        # for each line
        for p in range(len(line) - 1):
            # get points
            x1 = line[p][0]
            y1 = line[p][1]
            x2 = line[p+1][0]
            y2 = line[p+1][1]

            # check for low point
            global MAX
            if y1 > MAX:
                MAX = y1

            # get directrion
            if x2 - x1 > 0:
                dx = 1
            else:
                dx = -1
            if y2 - y1 > 0:
                dy = 1
            else:
                dy = -1

            # add lines
            for x in range(abs(x2-x1)+1):
                grid[y1][(x1+(x*dx))-XOFF] = "#"
            for y in range(abs(y2-y1)+1):
                grid[y1+(y*dy)][x1-XOFF] = "#"

    MAX+=2

def simulate(grid):
    NotDone    = True
    num        = 0
    global MAX
    while(NotDone):
        isFalling = True
        sand      = [0,500]
        num += 1
        while(isFalling):
            
            # at floor
            if sand[0] == MAX-1:
                grid[sand[0]][sand[1]-XOFF] = "o"
                isFalling = False

            # check below
            elif grid[sand[0]+1][sand[1]-XOFF] == ".":
                sand[0] += 1
            # check left diag
            elif grid[sand[0]+1][sand[1]-1-XOFF] == ".":
                sand[0] += 1
                sand[1] -= 1
            # check right diag
            elif grid[sand[0]+1][sand[1]+1-XOFF] == ".":
                sand[0] += 1
                sand[1] += 1
            # no more moves
            else:
                if sand[0] == 0 and sand[1] == 500:
                    NotDone = False
                grid[sand[0]][sand[1]-XOFF] = "o"
                isFalling = False

    return num

def main():
    grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
    points = []
    while (line:=sys.stdin.readline().strip()):
        points.append(list(map(lambda line: (int(line.split(",")[0]), int(line.split(",")[1])), line.split(" -> "))))

    add_lines(grid, points)
    print(simulate(grid))

    #for g in grid:
    #    print(g)

if __name__ == "__main__":
    main()
