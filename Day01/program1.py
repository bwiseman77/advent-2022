#! /usr/bin/env python3
import sys

def main():

    elf_temp = 0
    top_elfs = [0,0,0]


    line = sys.stdin.readline().strip()
    while(line := sys.stdin.readline()):
        if line.strip():
            elf_temp += int(line)
        
        else: 
            if(elf_temp >= top_elfs[0]):
                top_elfs[0], top_elfs[1], top_elfs[2] = elf_temp, top_elfs[0], top_elfs[1]
            elif(elf_temp >= top_elfs[1]):
                top_elfs[1], top_elfs[2] = elf_temp, top_elfs[1]
            elif(elf_temp >= top_elfs[2]):
                top_elfs[2] = elf_temp

            elf_temp = 0

    if(elf_temp >= top_elfs[0]):
        top_elfs[0], top_elfs[1], top_elfs[2] = elf_temp, top_elfs[0], top_elfs[1]
    elif(elf_temp >= top_elfs[1]):
        top_elfs[1], top_elfs[2] = elf_temp, top_elfs[1]
    elif(elf_temp >= top_elfs[2]):
        top_elfs[2] = elf_temp

    print(f"max number: {top_elfs[0] + top_elfs[1] + top_elfs[2]}")


        
if __name__ == "__main__":
    main()
