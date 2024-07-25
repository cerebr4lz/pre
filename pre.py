# Python Reg-Ex Library
# cerebr4l 2024

def is_literal(char):
    return char.isalpha() or char.isdigit()

def is_star(char):
    return char == '*'

def is_plus(char):
    return char == '+'

def is_qstn(char):
    return char == '?'

def is_oper(char):
    return is_star(char) or is_plus(char) or is_qstn(char)

def is_set_open(char):
    return char == '['

def is_set_close(char):
    return char == ']'

def is_grp_open(char):
    return char == '{'

def is_grp_close(char):
    return char == '}'

def is_match(expr, string):
    return expr[0] == string[0]

def split_expr(expr):
    head = None
    oper = None
    rest = None
    beg_pos = 0
    end_pos = 0
    
    if is_set_open(expr[0]):
        end_pos = expr.find(']')+1
        head = expr[beg_pos:end_pos]
    elif is_grp_open(expr[0]):
        end_pos = expr.find('}')+1
        head = expr[beg_pos:end_pos]
    elif is_literal(expr[0]):
        end_pos = 1
        head = expr[0]
    if is_oper(expr[end_pos]):
        oper = expr[end_pos]
        end_pos+=1

    rest = expr[end_pos:]

    return head, oper, rest

def match_expr(expr, string, match_len = 0):
    if len(expr) == 0:
        return [True, match_len]

    head, oper, rest = split_expr(expr)

    

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
