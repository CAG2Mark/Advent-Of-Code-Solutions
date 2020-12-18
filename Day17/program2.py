import copy

slices = []
slices_new = []

def gen_empty_3(xy, z):
    a = list()
    for i in range(z):
        a.append(gen_empty_2(xy))
    return a

def gen_empty_2(xy):
    b = list()
    for i in range(xy):
        b.append(['.']*(xy))
    return(b)

def expand():

    for s in slices:

        for xs in s:

            for xy in xs:
                xy.insert(0, '.')
                xy.append('.')

            xs.insert(0, ['.']*len(xs[0]))
            xs.append(['.']*len(xs[0]))

        s.insert(0, gen_empty_2(len(s[0])))
        s.append(gen_empty_2(len(s[0])))

    slices.insert(0, gen_empty_3(len(slices[0][0]), len(slices[0])))
    slices.append(gen_empty_3(len(slices[0][0]), len(slices[0])))
    

def do_cycle():
    for w in range(len(slices)):
        for z in range(len(slices[w])):
            for y in range(len(slices[w][z])):
                for x in range(len(slices[w][z][y])):
                    modify(x, y, z, w)


def modify(x, y, z, w):

    val = slices[w][z][y][x]

    min_x = max(0, x - 1)
    max_x = min(len(slices[0][0][0]), x + 2)

    min_y = max(0, y - 1)
    max_y = min(len(slices[0][0]), y + 2)

    min_z = max(0, z - 1)
    max_z = min(len(slices[0]), z + 2)

    min_w = max(0, w - 1)
    max_w = min(len(slices), w + 2)
    
    
    active_cnt = 0
    for x_ in range(min_x, max_x):
        for y_ in range(min_y, max_y):
            for z_ in range(min_z, max_z):
                for w_ in range(min_w, max_w):
                    if x_ == x and y_ == y and z == z_ and w == w_: continue

                    #print("{}, {}, {}, {}".format(x_, y_, z_, w_))

                    check = slices[w_][z_][y_][x_]
                    active_cnt += check == '#'

    if val == '#' and not 2 <= active_cnt <= 3:
        slices_new[w][z][y][x] = '.'
    elif val == '.' and active_cnt == 3:
        slices_new[w][z][y][x] = '#'
                


initial = []

while True:
    try:
        initial.append(list(input()))
    except EOFError:
        break

cur3d = list()
cur3d.append(gen_empty_2(len(initial)))
cur3d.append(initial)
cur3d.append(gen_empty_2(len(initial)))

slices.append(gen_empty_3(len(cur3d[0]), len(cur3d)))
slices.append(cur3d)
slices.append(gen_empty_3(len(cur3d[0]), len(cur3d)))

for i in range(6):
    expand()
    slices_new = copy.deepcopy(slices)
    do_cycle()
    slices = slices_new

cnt = 0
for w in range(len(slices)):
    for z in range(len(slices[0])):
        for y in range(len(slices[0][0])):
            for x in range(len(slices[0][0][0])):
                cnt += slices[w][z][y][x] == '#'
                
                

print(cnt)

