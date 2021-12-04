#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 4 Part 1
# -----------------------------------------------------------------------------

def checkboard(board, picks):
    cols = list(zip(*board))
    for row in board:
        if len([x for x in row if x in picks]) == len(row) and len(row) != 0:
            return True
    for col in cols:
        if len([x for x in col if x in picks]) == len(row) and len(row) != 0:
            return True
    return False

def find_first_win(boards, picks):
    for i in range(0, len(picks)):
        for board in boards:
            if checkboard(board, picks[:i]):
                return (board, picks[:i])
    return None

def calc_score(board, picks):
    unmarked = [x for x in sum(board, []) if x not in picks]
    return sum(unmarked) * picks[-1]

def main():
    with open('input.txt') as infile:
        lines = infile.read().split('\n\n')
        picks = [int(x) for x in lines[0].split(',')]

        # deal with it
        boards = [[[int(z) for z in y.split()] for y in x.split('\n')] for x in lines[1:]]

        win_board, win_picks = find_first_win(boards, picks)
        print(f'win board: {win_board}, win picks: {win_picks}')
        print(calc_score(win_board, win_picks))

if __name__ == '__main__':
    main()
