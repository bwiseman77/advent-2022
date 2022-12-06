#! /usr/bin/env python3
import sys

def sub(line):
    window = []
    for i, letter in enumerate(list(line)):
        window.append(letter)
        if len(window) < 4:
            continue

        print(window)

        if(len(set(window)) == 4):
            return i

        window.pop(0)


def main():
    while (line:=sys.stdin.readline().strip()):
        print(sub(line)+1)
        

if __name__ == "__main__":
    main()
