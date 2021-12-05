#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 5 Part 2
# -----------------------------------------------------------------------------

def maxind(coords, index):
    return max([max(x[0][index], x[1][index]) for x in coords])

def plot_line(plot, x0, y0, x1, y1):
    # Bresenham's line algorithm! Probably the most complicated part of this
    # as we need to deal with lines in either direction (increasing /or/
    # decreasing)
    dx = abs(x1 - x0)
    sx = 1 if x0 < x1 else -1
    dy = -abs(y1 - y0)
    sy = 1 if y0 < y1 else -1
    err = dx + dy

    while True:
        plot[x0][y0] += 1

        if x0 == x1 and y0 == y1:
            break

        e2 = err * 2
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

def main():
    with open('input.txt') as infile:
        lines = infile.read().split('\n')
        coords = [[[int(x) for x in coord.split(',')] for coord in line.split(' -> ')] for line in lines if line != '']

        max_x = maxind(coords, 0)
        max_y = maxind(coords, 1)

        # this is definitely not the most efficient way to implement this
        # problem, but it is pretty straightforward which is nice :)
        plot = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

        for line in coords:
            start, end = line
            start_x, start_y = start
            end_x, end_y = end

            plot_line(plot, start_x, start_y, end_x, end_y)

        # nice for debugging
        #for y in range(0, max_y + 1):
        #    for x in range(0, max_x + 1):
        #        print(f'{plot[x][y]} ', end='')
        #    print('')

        print(sum([1 for val in sum(plot, []) if val >= 2]))

if __name__ == '__main__':
    main()
