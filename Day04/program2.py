#! /usr/bin/env python3
import sys

def main():
    count = 0
    while (line:=sys.stdin.readline().strip()):
        I1,I2 = line.split(",")

        r1 = I1.split("-")
        r2 = I2.split("-")
        
        # 2-8,6-10
        
        if(int(r1[0]) <= int(r2[1]) and int(r1[0]) >= int(r2[0])):
            count += 1
        elif(int(r1[1]) >= int(r2[0]) and int(r1[1]) <= int(r2[1])):
            count += 1
        elif(int(r2[0]) <= int(r1[1]) and int(r2[0]) >= int(r1[0])):
            count += 1
        elif(int(r2[1]) >= int(r1[0]) and int(r2[1]) <= int(r1[1])):
            count += 1


    print(count)
           

if __name__ == "__main__":
    main()
