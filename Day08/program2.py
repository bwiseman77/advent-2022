#! /usr/bin/env python3
import sys

def func(row, col, trees):
    L, W = len(trees), len(trees[0])
    print(f"checking {trees[row][col]}:")
    r, l, u, d = 0,0,0,0
    # up
    for up in range(row-1, -1, -1):
        if trees[up][col] < trees[row][col]:
            u += 1
        else:
            u += 1
            break
    # down
    for dn in range(row+1, W):
        if trees[dn][col] < trees[row][col]:
            d += 1
        else:
            d += 1
            break

    # right
    for rt in range(col+1, L):
        if trees[row][rt] < trees[row][col]:
            r += 1
        else:
            r += 1
            break

    # left
    for lt in range(col-1, -1 ,-1):
        if trees[row][lt] < trees[row][col]:
            l += 1
        else:
            l += 1
            break

    if row == 0:
        u = 0
    if row == L-1:
        d = 0
    if col == 0:
        l = 0
    if col == W-1:
        r = 0

    print(f"score of {trees[row][col]}: {r}*{l}*{u}*{d}")
    return r*l*u*d


def main():
    trees = [[int(tree) for tree in line.strip()] for line in sys.stdin]
    l, w = len(trees), len(trees[0])

    score = 0
    for row in range(l):
        for col in range(w):
            score = max(score,func(row, col, trees))
    
    print(trees)
    print(score) 

if __name__ == "__main__":
    main()
