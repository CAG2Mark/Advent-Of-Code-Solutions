pos_x = 0
pos_y = 0

wp_x = 10
wp_y = -1

def mv_wp(val):
    if val == 0: return

    global wp_x, wp_y
    if val > 3:
        val //= 90
    val %= 4
    
    temp = wp_x
    wp_x = -wp_y
    wp_y = temp

    mv_wp(val - 1)

        
while True:
    try:
        ln = input()
        dir = ln[0]
        val = int(ln[1:])

        if dir == 'N':
            wp_y -= val
        elif dir == 'E':
            wp_x += val
        elif dir == 'S':
            wp_y += val
        elif dir == 'W':
            wp_x -= val
        elif dir == 'F':
            pos_x += val * wp_x
            pos_y += val * wp_y
        elif dir == 'L':
            mv_wp(360 - val)
        elif dir == 'R':
            mv_wp(val)

    except EOFError:
        break

print(abs(pos_x) + abs(pos_y))



