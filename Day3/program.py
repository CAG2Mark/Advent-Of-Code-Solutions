count = 0

area = list()

N = 0
L = 0

while True:
    ln = ""
    try:
        area.append(input())
        N = N + 1
    except EOFError:
        break

L = len(area[0])

x = 0
y = 0

while y < N:

    if area[y][x] == "#": count = count + 1

    x = (x + 3) % L
    y = y + 1

print(count)