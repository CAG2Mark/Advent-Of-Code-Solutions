bags = dict()

target = "shiny gold"

def add_bag(bag):
    if not bag in bags:
        x = list()
        bags[bag] = x
    return bags[bag]

def trim_bag_str(str):
    bag = str.strip().replace("bags", "").replace("bag", "").replace(".", "").strip()
    return (int(bag[0]), bag[2:])

sum = 0
def dfs(root, cur):
    global sum

    for x in bags[root]:
        sum = sum + cur * x[0]
        dfs(x[1], cur * x[0])

while True:
    ln = ""
    try:
        ln = input()
    except EOFError:
        break

    split = ln.split(" bags contain ")
    container = split[0] # The bag containing other bags
    contains = split[1]

    if contains == "no other bags.":
        add_bag(container)
        continue;


    _contains = [trim_bag_str(x) for x in split[1].split(", ")]

    _container = add_bag(container)

    for _bag in _contains:
        add_bag(_bag[1])
        _container.append(_bag);

dfs(target, 1)
print(sum)