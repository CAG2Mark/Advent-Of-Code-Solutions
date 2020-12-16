# valid ranges
rules = {}

# Input all the rules
while True:
    try:
        ln = input()
        if not ln.strip():
            break

        field = ln.split(": ")[0]
    
        rule = [x.split("-") for x in ln.split(": ")[1].split(" or ")]
        
        rules[field] = []
        for r in rule:
            rules[field].append(([int(x) for x in r]))
        
    except EOFError:
        break

# Input your ticket
input()
ticket = [int(x) for x in input().split(",")]
input()
input()

# Eliminate invalid tickets
valid = []
while True:
    try:
        ln = input()
        vals = [int(v) for v in ln.split(',')]

        flag = False
        for v in vals:
            if not any(r[0][0] <= v <= r[0][1] for r in rules.values()) and not any(r[1][0] <= v <= r[1][1] for r in rules.values()):
                flag = True
                break
        if not flag: valid.append(vals)
        
    except EOFError:
        break

indexes = {}

# Get all tickets that are possible for each key
keys = [*rules]

for k in keys:

    val = rules[k]

    i = []
    for x in range(len(rules.keys())):
        flag = False
        for y in range(len(valid)):
            v = valid[y][x]

            if not (val[0][0] <= v <= val[0][1] or val[1][0] <= v <= val[1][1]):
                flag = True
                continue

        if flag: continue
        i.append(x)

    indexes[k] = i

# Count the number of possible fields each column (data position) could belong to.
counts = {}
for vs in indexes.values(): # Reminder: indexes.values stores the possible column for each key
    for v in vs:
        if v in counts.keys():
            counts[v] += 1
        else:
            counts[v] = 1

# Sort the counts.
counts_s = sorted(counts, key=counts.get)

final = {}

# The idea here is to prioritise the columns that can belong to the fewest possible fields,
# then assign that to the field that has the least possible columns.
for c in counts_s:
    indexes_s = sorted(indexes, key=len)
    matches = [f for f in indexes_s if c in indexes[f]]
    final[matches[0]] = c

    indexes.pop(matches[0])

    for v in indexes.values():
        if c in v:
            v.remove(c)

prod = 1
for k in final.keys():
    if not "departure" in k: continue
    prod *= ticket[final[k]]

print(prod)
        