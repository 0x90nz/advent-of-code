#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 6 Part 2
# -----------------------------------------------------------------------------

import collections

# we can't be quite as naïve for this part ;)

def iterate_n(init, n):
    # we keep track of the number of fish in each state, instead of tracking
    # each individually
    state = collections.deque([0 for _ in range(0, 9)])
    for i in init:
        state[i] += 1

    # and then we can just iterate through the days, shifting around the deque
    # as needed
    for i in range(0, n):
        avail = state.popleft()
        state[-2] += avail
        state.append(avail)

    return sum(state)

def main():
    with open('input.txt') as infile:
        init = [int(x) for x in infile.read().split(',')]
        print(f'Initial state: {init}')

        print('nr with 80:  ', iterate_n(init, 80))
        print('nr with 256: ', iterate_n(init, 256))

if __name__ == '__main__':
    main()

