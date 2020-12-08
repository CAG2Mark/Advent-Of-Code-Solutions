acc = 0
inss = list()
visited = list()
N = 0

def run(index):
    global acc

    print(index)

    next_index = -1

    visited[index] = visited[index]

    ins = inss[index]

    ch = ins[0]
    val = int(ins[4:])
    if (ch == 'a'): #acc
        acc = acc + val
    elif (ch == 'j'): #jmp
        next_index = index + val

    if next_index == -1: next_index = index + 1

    if visited[next_index]:
        return

    
    if index >= N: return
    run(next_index)

while True:
    ln = ""
    try:
        inss.append(input())
        N = N + 1
    except EOFError:
        break

visited = [0] * N

print(acc)

run(0)
