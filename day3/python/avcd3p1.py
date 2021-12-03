#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 3 Part 1
# -----------------------------------------------------------------------------

def calc_gamma(lines):
    gamma = list('0' * 12)
    nr_lines = len(lines)
    for i in range(0, 12):
        bits = [x[i] for x in lines]
        if bits.count('1') > nr_lines / 2:
            gamma[i] = '1'
    return int(''.join(gamma), base=2)

def main():
    with open('input.txt') as infile:
        lines = infile.read().split()
        gamma = calc_gamma(lines)

        # epsilon is actually just the inversion of gamma (i.e. we choose bits
        # on the /exact/ inverse of the criteria for gamma), so we can just
        # invert the gamma value to get the epsilon value
        epsilon = gamma ^ 0b111111111111
        consumption = gamma * epsilon
        print(f'Gamma: {gamma}, Epsilon: {epsilon}, Consumption: {consumption}')

if __name__ == '__main__':
    main()
