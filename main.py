#!/usr/bin/env python3

import pre

def main():
    print(pre.split_expr('abc*'))
    print(pre.split_expr('*[123]bc'))
    print(pre.split_expr('a*bc'))
    print(pre.split_expr('[123]*jgs'))
    print(pre.split_expr('[abc]+j'))
    print(pre.split_expr('[aeiou]?y'))
    print(pre.split_expr('{123}*jgs'))
    print(pre.split_expr('{abc}+j'))
    print(pre.split_expr('{aeu}?y'))
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
