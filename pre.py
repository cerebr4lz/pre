# Python Reg-Ex Library
# cerebr4l 2024

def is_match(expr, string):
    return expr[0] == string[0]

def match_expr(expr, string, match_len = 0):
    if len(string) == 0:
        return [True, match_len]

    if is_match(expr, string):
        return match_expr(expr[1:], string[1:])
    else:
        return [False, None]
