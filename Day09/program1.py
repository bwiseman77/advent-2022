#! /usr/bin/env python3
import sys

def move_T(H, T, visited):
    dx = H[0] - T[0]
    dy = H[1] - T[1]

    # dont move
    if abs(dx) <= 1 and abs(dy) <= 1:
        pass
    elif dy == 0:
        T[0] += dx/2
    elif dx == 0:
        T[1] += dy/2
    elif abs(dy) == 2:
        T[0] += dx
        T[1] += dy/2
    elif abs(dx) == 2:
        T[0] += dx/2
        T[1] += dy

    visited.add((T[0], T[1]))


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
            H[1] += y
            move_T(H, T, visited)
    else:
        for n in range(num):
            H[0] += x
            move_T(H, T, visited)

def main():
    H = [0,0]
    T = [0,0]
    visited = set()

    while (line:=sys.stdin.readline().strip()):
        move, num = line.split()
        move_H(H, T, move, int(num), visited)

    print(H)
    print(T)
    print(len(visited))

if __name__ == "__main__":
    main()
