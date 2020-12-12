cur_dir = 1
pos_x = 0
pos_y = 0

def mv(dir, val):
    global pos_x, pos_y

    if dir == 0:
        pos_y -= val
    elif dir == 1:
        pos_x += val
    elif dir == 2:
        pos_y += val
    elif dir == 3:
        pos_x -= val

while True:
    try:
        ln = input()
        dir = ln[0]
        val = int(ln[1:])

        if dir == 'N':
            mv(0, val)
        elif dir == 'E':
            mv(1, val)
        elif dir == 'S':
            mv(2, val)
        elif dir == 'W':
            mv(3, val)
        elif dir == 'F':
            mv(cur_dir, val)
        elif dir == 'L':
            cur_dir = (cur_dir + (360 - val) // 90) % 4
        elif dir == 'R':
            cur_dir = (cur_dir + val // 90) % 4

    except EOFError:
        break

print(abs(pos_x) + abs(pos_y))



