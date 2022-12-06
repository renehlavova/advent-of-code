with open("2022/2022-12-04-input.txt", "r") as file:
    content = file.read()
    content_pairs = [
        [pair.split("-") for pair in line.split(",")]
        for line in content.strip().split("\n")
    ]


def get_full_overlap(pairs):
    """4-8 contains 4-5, or 5-6"""
    c = []

    for p in pairs:
        if (int(p[0][0]) <= int(p[1][0])) & (int(p[0][1]) >= int(p[1][1])) or (
            int(p[1][0]) <= int(p[0][0])
        ) & (int(p[1][1]) >= int(p[0][1])):
            c.append(p)

    return c


def get_all_overlaps(pairs):
    """4-8 contains 4-5, or 5-6, but also 3-4"""
    c = []

    for p in pairs:
        if int(p[0][0]) > int(p[1][0]):
            p = p[::-1]
        if int(p[0][1]) >= int(p[1][0]):
            c.append(1)

    return c

# scenario one
print(len(get_full_overlap(content_pairs)))

# scenario two
print(len(get_all_overlaps(content_pairs)))
