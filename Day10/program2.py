vts = list()
vts.append(0)

vtx = list()

total = 0

def dfs(cur, visited:list):
    global vtx, total

    if memo[cur] != -1:
        total += memo[cur]
        return
  
    if not vtx[cur]:
        if cur == tg + 3:
            total += 1
        return

    visited = visited.copy()
    visited.append(cur)
    
    for i in vtx[cur]:
        if not i in visited:
            dfs(i, visited)      
        

while True:
    try:
        vts.append(int(input()))
    except EOFError:
        break

tg = max(vts)
vts.append(tg + 3)
vts.sort()

vtx = [0]*(tg + 4)
memo = [-1]*(tg + 4)

cnt = len(vts) - 1

for i in range(cnt):
    vtx[vts[i]] = list()
    vtx[vts[i]].append(vts[i + 1])
    if i + 2 <= cnt and vts[i + 2] - vts[i] <= 3: vtx[vts[i]].append(vts[i+2])
    if i + 3 <= cnt and vts[i + 3] - vts[i] <= 3: vtx[vts[i]].append(vts[i+3])

for i in range(cnt + 1):
    if vtx[cnt - i] == 0: continue
    total = 0
    dfs(cnt - i, list())
    memo[cnt - i] = total

print(total)