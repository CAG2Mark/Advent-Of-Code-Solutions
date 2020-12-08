ids = list()
    
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

        ids.append(id)

    except EOFError:

        break

ids.sort()

for i in range(len(ids) - 1):
    if ids[i + 1] - ids[i] == 2:
        print(ids[i] + 1)
        break