import re
from pprint import pprint

with open("2022/2022-12-05-input.txt", "r") as file:
    data, instructions = file.read().split("\n\n")

instructions = [line for line in instructions.strip().split("\n")]

crates = re.findall(r".(.)..?", data)
crate_col = [crates[i : i + 9] for i in range(0, len(crates), 9)]
crate_t = list(map(list, zip(*crate_col)))
crate_ts = [[element for element in line if element.strip()] for line in crate_t]

for i in instructions:
    _, i, _, source, _, destination = i.split(" ")

    i = int(i)
    source = int(source) - 1
    destination = int(destination) - 1

    moved_items = [crate_ts[source][c] for c in range(i)]
    del crate_ts[source][:i]

    for m in reversed(moved_items):
        crate_ts[destination].insert(0, m)

for l in crate_ts:
    print(l[0])
