#!/usr/bin/env python3

import pre

def main():
    # print("Hello, World!")
    expr = 'abc'
    inpt = 'abc'
    [matched, matchlen] = pre.match_expr(expr, input)
    if matched:
        print(f'pre.match_expr({expr}, {input}) = True')
    else:
        print(f'pre.match_expr({expr}, {input}) = False')


if __name__ == '__main__':
    main()
