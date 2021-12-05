#!/usr/bin/env python3

# -----------------------------------------------------------------------------
# Advent of Code Day 5 Part 1
# -----------------------------------------------------------------------------

def maxind(coords, index):
    return max([max(x[0][index], x[1][index]) for x in coords])

def main():
    with open('input.txt') as infile:
        lines = infile.read().split('\n')
        coords = [[[int(x) for x in coord.split(',')] for coord in line.split(' -> ')] for line in lines if line != '']

        max_x = maxind(coords, 0)
        max_y = maxind(coords, 1)

        plot = [[0 for _ in range(max_y + 1)] for _ in range(max_x + 1)]

        for line in coords:
            start, end = line
            start_x, start_y = start
            end_x, end_y = end

            print(start_x, start_y, '->', end_x, end_y)

            # ignore diagonal lines
            if start_x == end_x or start_y == end_y:
                if start_x == end_x:
                    coord_min_y = min(start_y, end_y)
                    coord_max_y = max(start_y, end_y)
                    for i in range(coord_min_y, coord_max_y + 1):
                        print(f'{start_x}, {i}')
                        plot[start_x][i] += 1
                elif start_y == end_y:
                    coord_min_x = min(start_x, end_x)
                    coord_max_x = max(start_x, end_x)
                    for i in range(coord_min_x, coord_max_x + 1):
                        print(f'{i}, {start_y}')
                        plot[i][start_y] += 1

        for y in range(0, max_y + 1):
            for x in range(0, max_x + 1):
                print(f'{plot[x][y]} ', end='')
            print('')

        print(sum([1 for val in sum(plot, []) if val >= 2]))

if __name__ == '__main__':
    main()
