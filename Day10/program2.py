#! /usr/bin/env python3
import sys

Cycles = 0
RegX   = 1
C      = 40
Total  = 0
CRT = ["." for _ in range(40)]

def check():
    global C
    global Cycles
    global Total
    global CRT
    
    if Cycles == 40:
        print(CRT)
        Cycles = 0
        CRT = ["." for _ in range(40)]
    pos = Cycles % 40
    if pos == RegX or pos == RegX - 1 or pos == RegX + 1:
        CRT[pos] = "#"

    
def run(cmd, V):
    global Cycles
    global RegX
    check()
    if cmd == "noop":
        Cycles += 1

    elif cmd == "addx":
        Cycles += 1
        check()
        Cycles += 1
        RegX += V
    

def main():
    while (line:=sys.stdin.readline().strip()):
        l = line.split()
        V = 0
        cmd = l[0]
        if cmd == "noop":
            pass
        elif cmd == "addx":
            V = int(l[1])

        run(cmd, V)

    print(CRT)

if __name__ == "__main__":
    main()
