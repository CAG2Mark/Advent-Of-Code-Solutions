ques = [0] * 26
s = 0
cnt = 0    

def sum_cur():
    global s
    s = s + sum(x == cnt for x in ques)

while True:
    try:
        ln = input()
        if not ln.strip():
            sum_cur()
            ques = [0] * 26
            cnt = 0
            continue
            
        cnt = cnt + 1

        for ch in ln:
            i = ord(ch) - 97
            ques[i] = ques[i] + 1

    except EOFError:
        sum_cur()
        break

print(s)