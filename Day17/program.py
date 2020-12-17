import copy

slices = {}
slices_new = {}

cycle = 0

def expand():
    global cycle

    for s in slices.values():
        s.insert(0, ['.']*len(s[0]))
        s.append(['.']*len(s[0]))
    
        for r in s:
            r.insert(0, '.')
            r.append('.')

    slices[cycle + 2] = list()
    slices[-cycle - 2] = list()
    for i in range(len(slices[0][0])):
        slices[cycle + 2].append(['.']*len(slices[0][0]))
        slices[-cycle - 2].append(['.']*len(slices[0][0]))

def do_cycle():
    for z in slices.keys():
        sl = slices[z]
        for y in range(len(sl)):
            for x in range(len(sl[y])):
                modify(x, y, z)


def modify(x, y, z):

    val = slices[z][y][x]

    min_x = max(0, x - 1)
    max_x = min(len(slices[0][0]), x + 2)

    min_y = max(0, y - 1)
    max_y = min(len(slices[0]), y + 2)

    min_z = max(-cycle - 1, z - 1)
    max_z = min(cycle + 2, z + 2)
    
    active_cnt = 0
    for x_ in range(min_x, max_x):
        for y_ in range(min_y, max_y):
            for z_ in range(min_z, max_z):
                if x_ == x and y_ == y and z == z_: continue
                check = slices[z_][y_][x_]
                active_cnt += check == '#'

    if val == '#' and not 2 <= active_cnt <= 3:
        slices_new[z][y][x] = '.'
    elif val == '.' and active_cnt == 3:
        slices_new[z][y][x] = '#'
                


initial = []

while True:
    try:
        initial.append(list(input()))
    except EOFError:
        break

slices[1] = list()
slices[-1] = list()

for i in range(len(initial)):
    slices[1].append(['.']*len(initial))
    slices[-1].append(['.']*len(initial))

slices[0] = initial

for i in range(6):
    expand()
    slices_new = copy.deepcopy(slices)
    #print(slices)
    do_cycle()
    slices = slices_new
    cycle += 1

cnt = 0
for sl in slices.values():
    for y in sl:
        for x in y:
            cnt += x == '#'

print(cnt)

