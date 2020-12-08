max = 0
    
while True:
    try:
        ln = input()
        cur = 64
        row = 0

        for i in range(7):
            if ln[i] == 'B': row = row + cur
            cur = cur / 2

        cur = 4
        col = 0

        for i in range(7, 10):
            if ln[i] == 'R': col = col + cur
            cur = cur / 2

        id = row * 8 + col

        if max < id: max = id

    except EOFError:

        break

print(max)