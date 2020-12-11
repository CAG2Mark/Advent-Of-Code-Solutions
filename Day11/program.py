# Note: This is certainly my worst solution thus far. It is slow, long, and repetitive. This is in no way any representation of my best work.

import copy

seats = list()
seats_new = list()

def check_seat(x, y):
    cnt = 0
    lw_x = max(0, x - 1)
    up_x = min(x + 2, max_x)
    lw_y = max(0, y - 1)
    up_y = min(y + 2, max_y)
    for x_ in range(lw_x, up_x):
        for y_ in range(lw_y, up_y):
            if x_ == x and y_ == y: continue
            cnt += seats[y_][x_] == '#'

    return cnt

def do_round():
    for y in range(max_y):
        for x in range(max_x):
            if seats[y][x] == '.': continue;

            val = check_seat(x, y)
            if not val:
                seats_new[y][x] = '#'
            elif val >= 4:
                seats_new[y][x] = 'L'

def cnt_occupied():
    total = 0
    global seats
    for r in seats:
        total += r.count('#')
    return total

cntr = 0
while True:
    try:
        ln = input()
        seats.append(list())
        seats_new.append(list())
        for ch in ln:
            seats[cntr].append(ch)
            seats_new[cntr].append(ch)
        cntr += 1
    except EOFError:
        break

max_x = len(seats[0])
max_y = len(seats)

do_round()
cnt = 0
while seats != seats_new:
    seats = copy.deepcopy(seats_new)
    do_round()
    cnt += 1

print(cnt_occupied())



