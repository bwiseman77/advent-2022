#! /usr/bin/env python3
import sys

def main():
    
    ASCII_A = 65
    ASCII_a = 97
    total = 0
    while (line1:=sys.stdin.readline().strip()):
        line2 = set(sys.stdin.readline().strip())
        line3 = set(sys.stdin.readline().strip())

        value = 0
        for letter in line1:
            if letter in line2:
                if letter in line3:
                    value = ord(letter) - ASCII_a + 1 if letter.islower() else ord(letter) - ASCII_A + 27
                
        total += value

    print(total)

if __name__ == "__main__":
    main()
