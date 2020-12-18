from typing import Text


def eval_expr(expr:Text):
    expr = "+ " + expr
    is_add = False

    cur_val = 0

    pr_depth = 0
    pr_start = 0

    for i, ch in enumerate(expr):

        if ch == ' ': continue

        if ch == '(':
            pr_depth += 1
            if pr_depth == 1:
                pr_start = i + 1
        if ch == ')':
            pr_depth -= 1
            if pr_depth == 0:
                val = eval_expr(expr[pr_start:i])
                if is_add:
                    cur_val += val
                else:
                    cur_val *= val

        if pr_depth > 0: continue

        if ch == '+':
            is_add = True
        elif ch == '*':
            is_add = False

        if '0' <= ch <= '9':
            if is_add:
                cur_val += ord(ch) - ord('0');
            else:
                cur_val *= (ord(ch) - ord('0'));

    return cur_val
    
sum = 0

while True:
    try:
        ln = list(input())
        sum += eval_expr(input())

    except EOFError:
        break

print(sum)