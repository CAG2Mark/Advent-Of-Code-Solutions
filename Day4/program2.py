count = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
hex_not = "1234567890abcdef"

ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pprt(pprt):
    global count
    flag = True

    i = 0
    while flag and i < len(fields):
        flag = flag and fields[i] in pprt
        i = i + 1

    if flag:

        try:
            byr = int(pprt["byr"])
            flag = flag and (byr >= 1920 and byr <= 2002)

            iyr = int(pprt["iyr"])
            flag = flag and (iyr >= 2010 and iyr <= 2020)

            eyr = int(pprt["eyr"])
            flag = flag and (eyr >= 2020 and eyr <= 2030)

            hgt = int(pprt["hgt"][:-2])
            is_cm = pprt["hgt"][-2:] == "cm"
            lwr = 150 if is_cm else 59
            upr = 193 if is_cm else 76
            flag = flag and (hgt >= lwr and hgt <= upr)

            flag = flag and pprt["hcl"][0] == "#"
            for ch in pprt["hcl"][1:]:
                flag = flag and ch in hex_not

            flag = flag and pprt["ecl"] in ecls

            flag = flag and len(pprt["pid"]) == 9
        except:
            flag = False

    count = count + flag

    

pprt = dict()
    
while True:
    try:
        ln = input()
        if not ln.strip():
            check_pprt(pprt)
            pprt = dict()
            continue

        data = ln.split(" ")
        for d in data:
            d_spl = d.split(":")
            pprt[d_spl[0]] = d_spl[1]
    except EOFError:
        check_pprt(pprt)
        break

print(count)