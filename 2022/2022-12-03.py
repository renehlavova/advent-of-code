with open("2022/2022-12-03-input.txt", "r") as file:
    content = file.read()
    rucksacks = [rucksack for rucksack in content.strip().split("\n")]


def get_priorities(matches):
    """Convert string to integers (aka priorities)"""
    priorities = []

    for m in matches:
        if m[0].islower():
            priorities.append(ord(m[0]) - 96)
        elif m[0].isupper():
            priorities.append(ord(m[0]) - 65 + 27)

    return sum(priorities)


# scenario one
rucksacks_1 = [[r[: len(r) // 2], r[len(r) // 2 :]] for r in rucksacks]
matches_1 = [list(set(r[0]) & set(r[1])) for r in rucksacks_1]
print(get_priorities(matches_1))


# scenario two
rucksacks_2 = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
matches_2 = [list(set(r[0]) & set(r[1]) & set(r[2])) for r in rucksacks_2]
print(get_priorities(matches_2))
