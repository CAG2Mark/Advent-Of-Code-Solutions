ques = [0] * 26
sum = 0
    
while True:
    try:
        ln = input()
        if not ln.strip():
            ques = [0] * 26
            continue

        for ch in ln:
            i = ord(ch) - 97
            if not ques[i]: sum = sum + 1
            ques[i] = 1

    except EOFError:
        break

print(sum)