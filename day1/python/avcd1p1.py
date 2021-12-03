#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 1 Part 1
# -----------------------------------------------------------------------------

from functools import reduce

def main():
    with open('input.txt') as infile:
        lines = infile.read().split()
        prev = 9999
        count = 0
        for i in (int(line) for line in lines):
            if i > prev:
                count += 1
            prev = i
        print(count)


if __name__ == '__main__':
    main()

