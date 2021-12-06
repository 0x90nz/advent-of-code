#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 6 Part 1
# -----------------------------------------------------------------------------

TIMER_INIT = 8
TIMER_RESET = 6

def iterate_day(state):
    new_count = state.count(0)
    new_state = [x - 1 for x in state]
    new_state = [x if x != -1 else TIMER_RESET for x in new_state]
    new_state.extend([TIMER_INIT for _ in range(0, new_count)])
    return new_state

def iterate_n(init, n):
    state = init
    for i in range(0, n):
        state = iterate_day(state)
    return state

def main():
    with open('input.txt') as infile:
        init = [int(x) for x in infile.read().split(',')]
        print(f'Initial state: {init}')

    print(len(iterate_n(init, 80)))

if __name__ == '__main__':
    main()

