area = list()

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]

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

prod = 1

for slope in slopes:

    count = 0

    x = 0
    y = 0

    while y < N:

        if area[y][x] == "#": count = count + 1

        x = (x + slope[0]) % L
        y = y + slope[1]

    prod = prod * count

print(prod)