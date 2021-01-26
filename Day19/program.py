rules = {}

og_val = ""
def check_rule(rule, val):
    
    temp = rule
    
    rule = rules[rule]
    
    if isinstance(rule, str):
        if len(val) == 0: return (False, 1)
        #print("Check -> " + rule + ", " + val)
        return (rule == val[0], 1)
    
    for r in rule:
        
        pos = 0
        
        flag = True
        for ri in r:

            ri = int(ri)
            #print("{}, {}, {}, {}, {}".format(temp, ri, val, val[pos:], pos))
            check = check_rule(ri, val[pos:])
            #print("{}, {}, {}, {}".format(check[0], temp, ri, val[pos:]))
            flag = flag and check[0]
            if not flag: break
            
            pos += check[1]
            
        if flag: 
            if temp == 0:
                return (pos == (len(val)), pos)
            return (True, pos)
        else: continue
        
    return (False, -1)

# Generate rules
while True:
    try:
        ln = input()
        if not ln.strip(): break
        
        rule = ln.split(": ")
        
        if "\"" in rule[1]:
            rules[int(rule[0])] = rule[1][1]
        else:
            rules[int(rule[0])] = [x.split(" ") for x in rule[1].split(" | ")]

    except EOFError:
        break
    
print(rules)
    
    
cnt = 0
while True:
    try:
        og_val = input()
        cnt += check_rule(0, og_val)[0]

    except EOFError:
        break
    
print(cnt)