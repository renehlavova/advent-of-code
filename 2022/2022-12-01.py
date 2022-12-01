with open("2022/2022-12-01-input.txt", "r") as calories:
    content = calories.read()
    elf_list = [elves.split("\n") for elves in content.strip().split("\n\n")]

elf_sum = [sum((int(val) for val in elf)) for elf in elf_list]
elf_hero = max(elf_sum)
elf_top_three_heroes = sum(sorted(elf_sum, reverse=True)[:3])

print(elf_hero)
print(elf_top_three_heroes)