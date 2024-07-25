#!/usr/bin/env python3

import pre

def main():
    # print("Hello, World!")
    expr = 'abc'
    string = 'hello, world: abc - def'
    # matched = pre.match_expr(expr, string)
    [matched, pos, length] = pre.match(expr, string)
    if matched:
        print(f'({expr}, {string}) = {string[pos:pos + length]}')
    else:
        print(f'({expr}, {string}) = {string[length:]}')


if __name__ == '__main__':
    main()
