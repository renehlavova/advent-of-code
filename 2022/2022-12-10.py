with open("2022/2022-12-10-input.txt", "r") as file:
    lines = [line for line in file.read().strip().split("\n")]

# part one
cycle = 1
x = 1
cycles = []

for l in lines:
    if l == "noop":
        cycles.append([cycle, x])
        cycle += 1
    elif l.startswith("addx"):
        addx, value = l.split(" ")
        cycles.append([cycle, x])
        cycle += 1
        cycles.append([cycle, x])
        x += int(value)
        cycle += 1

signals = [20, 60, 100, 140, 180, 220]
signal_sum = sum([cycles[s - 1][0] * cycles[s - 1][1] for s in signals])
print(signal_sum)

# part two
hashtags = []

for cycle in cycles:
    if cycle[0] % 40 in range(cycle[1], cycle[1] + 3):
        hashtags.append("#")
    else:
        hashtags.append(".")

chunks = [hashtags[x : x + 40] for x in range(0, len(hashtags), 40)]

for chunk in chunks:
    print("".join([c if c == "#" else " " for c in chunk]))
