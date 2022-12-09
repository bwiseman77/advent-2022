#! /usr/bin/env python3
import sys

def func(i, j, trees, tall, visable):
    if trees[i][j] > tall:
        visable.add((i, j))
        return trees[i][j]
    else:
        return -1

def main():
    trees = [[int(tree) for tree in line.strip()] for line in sys.stdin]
    l, w = len(trees), len(trees[0])

    visable = set()
    for row in range(l):
        tall= -1
        
        # left
        print("left")
        for col in range(w):
            tall = max(tall, func(row, col, trees, tall, visable))
        
        # right
        print("right")
        tall = -1
        for col in range(w-1, -1, -1):
            tall = max(tall, func(row, col, trees, tall, visable))

    for col in range(w):
        tall= -1
        
        # top
        print("top")
        for row in range(l):
            tall = max(tall, func(row, col, trees, tall, visable))
        
        # bottom
        print("bottom")
        tall = -1
        for row in range(l-1, -1, -1):
            tall = max(tall, func(row, col, trees, tall, visable))

    print(len(visable))
        
        

if __name__ == "__main__":
    main()
