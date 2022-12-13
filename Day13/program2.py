#! /usr/bin/env python3
import sys
import functools

def check(L1, L2):
    # 1 means good, -1 means bad, 0 means idk 
    # check
    for i in range(len(L1)):
        l1 = L1[i]
        if i == len(L2):
            return -1
        l2 = L2[i]

        # check if numeric
        if isinstance(l1, int) and isinstance(l2, int):
            if l1 < l2:
                return 1
            elif l1 > l2:
                return -1
        elif isinstance(l1, list) and isinstance(l2, list):
            d = check(l1, l2)
            if d == 0:
                continue
            else:
                return d
        elif isinstance(l1, list) and isinstance(l2, int):
            d = check(l1, [l2])
            if d == 0:
                continue
            else:
                return d
        elif isinstance(l1, int) and isinstance(l2, list):
            d = check([l1], l2)
            if d == 0:
                continue
            else:
                return d

    # if we got through all, we should check length
    if len(L1) < len(L2):
        return 1
    elif len(L1) > len(L2):
        return -1
    else:
        return 0

def read_pair(num, Pairs):

    L1 = eval(sys.stdin.readline().strip())    
    L2 = eval(sys.stdin.readline().strip())

    Pairs.append(L1)
    Pairs.append(L2)


    if check(L1, L2) == 1:
        return num
    else:
        return 0

def main():
    Total = 0
    num = 1  
    Pairs = [[[2]], [[6]]]
    Total += read_pair(num, Pairs)
    while (line:=sys.stdin.readline()):
        num   += 1
        Total += read_pair(num, Pairs)

    Pairs.sort(reverse=True, key=functools.cmp_to_key(check))
    for p in Pairs:
        print(p)

    print((Pairs.index([[2]])+1) * (Pairs.index([[6]])+1))


        

if __name__ == "__main__":
    main()
