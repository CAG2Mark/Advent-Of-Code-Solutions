acc = 0
inss = list()
visited = list()
N = 0

def run(index):
    global acc

    next_index = -1

    if visited[index]:
        return
    visited[index] = 1

    ins = inss[index]

    ch = ins[0]
    val = int(ins[4:])
    if (ch == 'a'): #acc
        acc = acc + val
    elif (ch == 'j'): #jmp
        next_index = index + val

    if next_index == -1: next_index = index + 1
    
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

run(0)

print(acc)
