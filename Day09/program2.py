#! /usr/bin/env python3
import sys

SIZE = 10000
GRID = [["." for _ in range(SIZE)] for _ in range(SIZE)]

def print_grid():
    return
    for g in GRID:
        print(g)

    print()

def move_Ts(H, T, visited, n):
    if n > 8:
        return
    GRID[T[n][1]][T[n][0]] = "."
    dx = H[0] - T[n][0]
    dy = H[1] - T[n][1]

    # dont move
    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif dy == 0:
        T[n][0] += dx//2
    elif dx == 0:
        T[n][1] += dy//2
    elif abs(dy) == 2 and abs(dx) == 2:
        T[n][0] += dx//2
        T[n][1] += dy//2
    elif abs(dy) == 2:
        T[n][0] += dx
        T[n][1] += dy//2
    elif abs(dx) == 2:
        T[n][0] += dx//2
        T[n][1] += dy

    if n == 8:
        visited.add((T[n][0], T[n][1]))
    
    GRID[T[n][1]][T[n][0]] = str(n+1)

    move_Ts(T[n], T, visited, n+1)


def move_H(H, T, move, num, visited):
    x = 0
    y = 0
    if move == "R":
        x = 1
    if move == "L":
        x = -1
    if move == "U":
        y = 1
    if move == "D":
        y = -1

    if x == 0:
        for n in range(num):
            GRID[H[1]][H[0]] = "."
            H[1] += y
            GRID[H[1]][H[0]] = "H"
            move_Ts(H, T, visited, 0)
            print_grid()

    else:
        for n in range(num):
            GRID[H[1]][H[0]] = "."
            H[0] += x
            move_Ts(H, T, visited, 0)
            GRID[H[1]][H[0]] = "H"
            print_grid()

def main():
    H = [0,0]
    T = [[0,0] for _ in range(9)]
    visited = set()

    while (line:=sys.stdin.readline().strip()):
        move, num = line.split()
        move_H(H, T, move, int(num), visited)

    print(len(visited))

if __name__ == "__main__":
    main()
