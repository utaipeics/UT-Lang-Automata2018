#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
from tape import Direction
from tape import Tape

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('usage: {} <palindrome>'.format(sys.argv[0]))
        print('where the format of a palindrome is L = { ww^R | w = (0+1)^* }')
        sys.exit(0)

    tape = Tape(sys.argv[1])

    while True:
        if tape.read() == '0':
            tape.write('x')
            tape.move_head(Direction.RIGHT)

            if tape.read() in ['0', '1']:
                tape.move_head(Direction.RIGHT)
            elif tape.read() in ['x', 'y']:
                break

            while tape.read() in ['0', '1']:
                tape.move_head(Direction.RIGHT)

            if tape.read() in ['d', 'x', 'y']:
                tape.move_head(Direction.LEFT)

            if tape.read() == '0':
                tape.write('x')
                tape.move_head(Direction.LEFT)
            else:
                sys.exit(1)

            while tape.read() in ['0', '1']:
                tape.move_head(Direction.LEFT)

            if tape.read() == 'x':
                tape.move_head(Direction.RIGHT)

        elif tape.read() == '1':
            tape.write('y')
            tape.move_head(Direction.RIGHT)

            if tape.read() in ['0', '1']:
                tape.move_head(Direction.RIGHT)
            elif tape.read() in ['x', 'y']:
                break

            while tape.read() in ['0', '1']:
                tape.move_head(Direction.RIGHT)

            if tape.read() in ['d', 'x', 'y']:
                tape.move_head(Direction.LEFT)

            if tape.read() == '1':
                tape.write('y')
                tape.move_head(Direction.LEFT)
            else:
                sys.exit(1)

            while tape.read() in ['0', '1']:
                tape.move_head(Direction.LEFT)

            if tape.read() == 'y':
                tape.move_head(Direction.RIGHT)

        elif tape.read() in ['d', 'x', 'y']:
            break

    print('The string {} is a palindrome'.format(sys.argv[1]))
