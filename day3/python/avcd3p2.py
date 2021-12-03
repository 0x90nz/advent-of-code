#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 3 Part 2
# -----------------------------------------------------------------------------

def calc_gamma(lines, word_len):
    gamma = list('0' * word_len)
    nr_lines = len(lines)
    for i in range(0, word_len):
        bits = [x[i] for x in lines]
        if bits.count('1') > nr_lines / 2:
            gamma[i] = '1'
    return int(''.join(gamma), base=2)

def calc_life(lines, word_len, oxy):
    candidates = lines[:]
    i = 0
    while len(candidates) > 1 and i < word_len:
        nr_candidates = len(candidates)
        if oxy:
            bit = '1' if [x[i] for x in candidates].count('1') >= nr_candidates / 2 else '0'
        else:
            bit = '0' if [x[i] for x in candidates].count('0') <= nr_candidates / 2 else '1'
        candidates = [c for c in candidates if c[i] == bit]
        i += 1
    return candidates[0]

def main():
    with open('input.txt') as infile:
        lines = infile.read().split()
        word_len = len(lines[0])
        gamma = calc_gamma(lines, word_len)

        # epsilon is actually just the inversion of gamma (i.e. we choose bits
        # on the /exact/ inverse of the criteria for gamma), so we can just
        # invert the gamma value to get the epsilon value
        epsilon = gamma ^ ((2 ** word_len) - 1)
        consumption = gamma * epsilon
        print(f'Gamma: {gamma}, Epsilon: {epsilon}, Consumption: {consumption}')

        oxy = int(calc_life(lines, word_len, True), base=2)
        co2 = int(calc_life(lines, word_len, False), base=2)
        life = oxy * co2
        print(f'Oxygen: {oxy}, CO2: {co2}, Life support: {life}')


if __name__ == '__main__':
    main()
