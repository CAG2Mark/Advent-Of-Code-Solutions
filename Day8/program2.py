inss = list()
N = 0

def run(index, acc, visited, used):

    if index == N:
        print(acc)
        return
    
    if index < 0 or index > N:
        return

    visited = visited.copy()

    if index in visited: return

    visited.append(index)

    ins = inss[index]

    ch = ins[0]
    val = int(ins[4:])
    if (ch == 'a'): #acc
        acc = acc + val
    elif (ch == 'j'): #jmp
        run(index + val, acc, visited, used)
        if not used:
            run(index + 1, acc, visited, True) #mulate nop
        return
    elif (ch == 'n'): #nop
        run(index + 1, acc, visited, used)
        if not used:
            run(index + val, acc, visited, True) #emulate jmp
        return

    run(index + 1, acc, visited, used)

while True:
    ln = ""
    try:
        inss.append(input())
        N = N + 1
    except EOFError:
        break

run(0, 0, list(), False)
