#! /usr/bin/env python3
import sys

def main():
    
    ASCII_A = 65
    ASCII_a = 97
    total = 0
    while (line:=sys.stdin.readline().strip()):
        l = int(len(line)/2)
        front, back = line[:l], line[l:]
        print(front, "|", back)

        value = 0
        for letter in front:
            if letter in back:
                value = ord(letter) - ASCII_a + 1 if letter.islower() else ord(letter) - ASCII_A + 27
                
        total += value

    print(total)

if __name__ == "__main__":
    main()
