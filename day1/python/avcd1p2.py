#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 1 Part 2
# -----------------------------------------------------------------------------

from functools import reduce

def main():
    with open('input.txt') as infile:
        nums = [int(line) for line in infile.read().split()]
        prev = 9999999
        count = 0
        for i in range(0, len(nums) - 2):
            val = sum(nums[i:i+3])
            if val > prev:
                count += 1
            prev = val
        print(count)


if __name__ == '__main__':
    main()

