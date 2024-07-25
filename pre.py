# Python Reg-Ex Library
# cerebr4l 2024

def is_literal(char):
    return char.isalpha() or char.is_digit()

def is_object(char):
    match char:
        case '[':
            return 'open set ['
        case _:
            return False

def is_match(expr, string):
    return expr[0] == string[0]

def match_expr(expr, string, match_len = 0):
    if len(expr) == 0:
        return [True, match_len]

    if is_match(expr, string):
        return match_expr(expr[1:], string[1:], match_len+1)
    else:
        return [False, None]

def match(expr, string):
    pos = 0
    max_len = len(string)-1
    matched = False
    while not matched and pos < max_len:
        [matched, length] = match_expr(expr, string[pos:])
        if matched:
            return [matched, pos, length]
        pos += 1
    return [False, None, None]
