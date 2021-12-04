#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 4 Part 2
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

def find_last_win(boards, picks):
    # this is a really naïve approach, and I'm certain there's a better way,
    # but it's late on Saturday; what do you want from me...
    done = []
    doneidx = []
    for i in range(0, len(picks)):
        for j in (x for x in range(0, len(boards)) if x not in done):
            if checkboard(boards[j], picks[:i]):
                done.append(j)
                doneidx.append(i)
    return (boards[done[-1]], picks[:doneidx[-1]])

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

        lose_board, lose_picks = find_last_win(boards, picks)
        print(f'lose board: {lose_board}, lose picks: {lose_picks}')
        print(calc_score(lose_board, lose_picks))


if __name__ == '__main__':
    main()
