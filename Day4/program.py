count = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_pprt(pprt):
    global count
    flag = True

    i = 0
    while flag and i < len(fields):
        flag = flag and fields[i] in pprt
        i = i + 1

    count = count + flag

pprt = ""
    
while True:
    try:
        ln = input()
        if not ln.strip():
            check_pprt(pprt)
            pprt = ""
            continue

        pprt = pprt + ln
    except EOFError:
        check_pprt(pprt)
        break

print(count)