bags = dict()

target = "shiny gold"


def add_bag(bag):
    if not bag in bags:
        x = list()
        bags[bag] = x
    return bags[bag]

def trim_bag_str(str):
    return str.strip().replace("bags", "").replace("bag", "").replace(".", "").strip()[2:]

found = 0
def dfs(root, visited):
    global found
    if root == target:
        found = -1
    found = found + 1
    visited.append(root)
    for x in bags[root]:
        if not x in visited:
            dfs(x, visited)

while True:
    ln = ""
    try:
        ln = input()
    except EOFError:
        break

    split = ln.split(" bags contain ")
    container = split[0] # The bag containing other bags
    contains = split[1]

    if contains == "no other bags": continue

    _contains = [trim_bag_str(x) for x in split[1].split(", ")]

    add_bag(container)

    for _bag in _contains:
        add_bag(_bag).append(container)

dfs(target, list())
print(found)


    
        
