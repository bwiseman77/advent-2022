#! /usr/bin/env python3
import sys

def main():

    # read inital stacks
    num_crates = 0
    num_stacks = 0
    lines = []
    while (line:=sys.stdin.readline().strip("\n")):
        if "1" in line:
            num_stacks = int(line.strip().split(" ")[-1])
            break;
        num_crates += 1
        lines.append(line)


    # build stacks
    list_o_stacks = []
    for i in range(num_stacks):
        stack = []
        for j in range(num_crates):
            if i == 0:
                index = 1
            else:
                index = (4*i) + 1

            if lines[j][index] != " ":
                stack.append(lines[j][index])
        
        stack.reverse()
        list_o_stacks.append(stack)

    print(list_o_stacks)

    # read newline
    sys.stdin.readline()

    # do the moves, top of
    while (line:=sys.stdin.readline().strip()):
        l = line.split(" ")
        num, src, dest = int(l[1]), int(l[3])-1, int(l[5])-1

        for i in range(num):
            crate = list_o_stacks[src].pop()
            list_o_stacks[dest].append(crate)

    for i in range(num_stacks):
        print(list_o_stacks[i][-1],end="");
    print("")


if __name__ == "__main__":
    main()
