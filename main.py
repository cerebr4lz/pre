#!/usr/bin/env python3

import pre

def main():
    # print("Hello, World!")
    expr = 'abz'
    string = 'abc'
    # matched = pre.match_expr(expr, string)
    matched, length = pre.match_expr(expr, string)
    if matched:
        print(f'({expr}, {string}: len({length})) = True')
    else:
        print(f'({expr}, {string}): len({length})) = False')


if __name__ == '__main__':
    main()
