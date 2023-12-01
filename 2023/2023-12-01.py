import re

def find_first_last_digit(line):
    """Find first and last number in a line, number represented as digit"""
    digits = list(filter(str.isdigit, line))
    return digits[0]+digits[-1]

def find_index_of_number(line):
    """Find numbers in a line with associated indexes"""
    n_index = {}
    number_pairs = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for key, value in number_pairs.items():
        pattern = re.compile(f"{key}|{value}")
        matches = [match.start() for match in re.finditer(pattern, line)]
    
        if matches:
            n_index[value] = matches
    return n_index

def find_first_last_number(n_index):
    """Find first and last number based on indexes, taking into account word representation of number"""
    all_indices = [index for indices in n_index.values() for index in indices]
    first_index = min(all_indices)
    last_index = max(all_indices)
    first_key = next(key for key, indices in n_index.items() if first_index in indices)
    last_key = next(key for key, indices in n_index.items() if last_index in indices)
    return first_key+last_key


file_path = "2023/2023-12-01-input.txt"

first_last_part_one = []
first_last_part_two = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        # part 1
        first_last_part_one.append(find_first_last_digit(line))
        # part 2
        n_index = find_index_of_number(line)
        first_last_part_two.append(find_first_last_number(n_index))
    
print(sum(map(int, first_last_part_one)))
print(sum(map(int, first_last_part_two)))
