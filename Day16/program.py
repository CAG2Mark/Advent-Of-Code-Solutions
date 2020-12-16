# valid ranges
rules = []

while True:
    try:
        ln = input()
        if not ln.strip():
            break
    
        rule = [x.split("-") for x in ln.split(": ")[1].split(" or ")]
        for r in rule:
            rules.append([int(x) for x in r])
        
    except EOFError:
        break

while True:
    if not input().strip(): break

input()
inval_sum = 0
while True:
    try:
        ln = input()
        vals = ln.split(',')
        for v in vals:
            if not any(r[0] <= int(v) <= r[1] for r in rules):
                inval_sum += int(v)
        
    except EOFError:
        break

print(inval_sum)