from typing import Text


def eval_expr(expr:Text):
    expr = list(expr)

    pr_depth = 0
    pr_start = 0

    while '(' in expr:
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

                    expr = expr[:(pr_start - 1)] + [str(val)] + expr[(i + 1):]
                    break

    while '+' in expr:
        for i, ch in enumerate(expr):

            if ch == '+':
        
                l = i - 2
                r = i + 2
                lv = int(expr[i-2])
                rv = int(expr[i+2])

                expr = expr[:l] + [str(lv + rv)] + expr[r + 1:]

                break

    expr = list(''.join(expr).split(" * "))

    prod = 1
    for i in expr:
        prod *= int(i)

    return prod
    
sum = 0
while True:
    try:
        sum += eval_expr(input())

    except EOFError:
        break

print(sum)