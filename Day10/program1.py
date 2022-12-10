#! /usr/bin/env python3
import sys

Cycles = 0
RegX   = 1
C      = 20
Total  = 0
def check():
    global C
    global Cycles
    global Total
    if Cycles == C:
        Total += RegX * C
        print(C, RegX, RegX*C)
        C += 40

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
        check()
        RegX += V
    check()
    

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

    print(Total)

if __name__ == "__main__":
    main()
