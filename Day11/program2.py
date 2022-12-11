#! /usr/bin/env python3
import sys
import math
Rounds = 10000

def read_monkey(Monkeys, MonkeyB, line):
    # monkey number
    num     = int(line.split(" ")[1].split(":")[0])
    items   = list(map(int, sys.stdin.readline().strip().split(":")[1].split(",")))
    op      = sys.stdin.readline().strip().split(":")[1]
    test    = int(sys.stdin.readline().strip().split(":")[1].split(" ")[-1])
    ifTrue  = int(sys.stdin.readline().strip().split(" ")[-1])
    ifFalse = int(sys.stdin.readline().strip().split(" ")[-1])
    sys.stdin.readline()

    #print("monkey num", num, "Monkey items:", items, "Monkey Op", op, "Monkey test", test, "ifTrue", ifTrue, "ifFalse", ifFalse)
    #(items, new worry, divis by, true throw to, false throw to)
    Monkeys[num] = [items, op, test, ifTrue, ifFalse]
    MonkeyB[num] = 0

def main():
    Monkeys = {}
    MonkeyB = {}
    MAX = 1
    while (line:=sys.stdin.readline().strip()):
        read_monkey(Monkeys, MonkeyB, line)

    
    for m in Monkeys.keys():
        MAX = MAX * Monkeys[m][2]

    print(MAX)

    for r in range(Rounds):
        
        for monkey in Monkeys.keys():

            while (l := Monkeys[monkey][0]):
                item = l.pop(0)
                #print("item tp inspect", item)
                MonkeyB[monkey] += 1
            
                # do op
                v1 = Monkeys[monkey][1].split(" ")[3]
                op = Monkeys[monkey][1].split(" ")[4]
                v2 = Monkeys[monkey][1].split(" ")[5]

                if v1 == "old":
                    v1 = item
                else:
                    v1 = int(v1)
                if v2 == "old":
                    v2 = item
                else:
                    v2 = int(v2)

                if op == "*":
                    item = v1 * v2
                elif op == "+":
                    item = v1 + v2
            
                #print("new item", item)
                
                #update worry
                item %= MAX

                #print("relief", item)
                # check div
                div = Monkeys[monkey][2]
                if item % div == 0:
                    # throw to true
                    #print("throw to monkey", Monkeys[monkey][3])
                    Monkeys[Monkeys[monkey][3]][0].append(item)
                else:
                    # throw to false
                    #print("throw to monkey", Monkeys[monkey][4])
                    Monkeys[Monkeys[monkey][4]][0].append(item)

        #print(Monkeys)
    
    #print(MonkeyB)

    m = [0,0]
    for monkey in MonkeyB.keys():
        c = MonkeyB[monkey]
        if c > m[0]:
            m[0], m[1] = c, m[0]
        elif c > m[1]:
            m[1] = c
    print(MonkeyB)
    print(m[0] * m[1])


if __name__ == "__main__":
    main()
