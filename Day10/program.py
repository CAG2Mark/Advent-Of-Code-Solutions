vts = list()
vts.append(0)
diff = list()

while True:
    try:
        vts.append(int(input()))
    except EOFError:
        break

tg = max(vts)
vts.append(tg + 3)
vts.sort()

print(vts)

for i in range(len(vts) - 1):
    diff.append(vts[i+1] - vts[i])

print(diff.count(1) * diff.count(3))
