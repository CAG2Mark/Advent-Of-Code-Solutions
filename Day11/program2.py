# Note: This is certainly my worst solution thus far. It is slow, long, and repetitive. This is in no way any representation of my best work.

import copy

seats = list()
seats_new = list()

def check_seat(x, y):

    global max_x, max_y
    cnt = 0
    for i in range(0, 9):
        dx = i % 3 - 1
        dy = (i // 3) - 1

        if not dx and not dy: continue

        x_ = x
        y_ = y

        while True:

            x_ += dx
            y_ += dy

            if not (0 <= x_ < max_x and 0 <= y_ < max_y): break

            if seats[y_][x_] == '.': continue
            if seats[y_][x_] == '#':
                cnt += 1;
            break;

    return cnt

def do_round():
    for y in range(max_y):
        for x in range(max_x):
            if seats[y][x] == '.': continue;

            val = check_seat(x, y)
            if not val:
                seats_new[y][x] = '#'
            elif val >= 5:
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



