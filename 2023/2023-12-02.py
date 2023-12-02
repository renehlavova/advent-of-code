import re

file_path = "2023/2023-12-02-input.txt"
max_counts = {'red': 12, 'blue': 14, 'green': 13}
game_dict = {}
total_max_power = 0
valid_game_ids = []

def parse_game_line(line):
    """Parse a line of the input file into a game id and a list of elements"""
    id, elements = line.strip().split(": ")
    return id.replace("Game ", ""), elements.split("; ")

def extract_number_color_pairs(value):
    """Extract number-color pairs from a list of elements"""
    return [(int(match.group(1)), match.group(2)) for sublist in value for match in re.finditer(r'(\b\d+\b)\s*(\w+)', sublist)]

def calculate_max_line(number_color_pairs):
    """Calculate the maximum color number per line for a list of number-color pairs"""
    max_line = {}
    for number, color in number_color_pairs:
        current_max = max_line.get(color, float('-inf'))
        max_line[color] = max(current_max, number)
    return max_line

def is_valid_game(max_line, max_counts):
    """Check if a game is valid based on the maximum color numbers per line compared to the threshold"""
    return all(max_line[key] <= max_counts[key] for key in max_line)

def calculate_game_power(max_line):
    """Calculate the power of a game based on the maximum color numbers per line"""
    return max_line['red'] * max_line['green'] * max_line['blue']

with open(file_path, "r") as file:
    for line in file:
        game_id, elements = parse_game_line(line)
        game_dict[game_id] = elements

    colors = ['red', 'blue', 'green']

    for key, value in game_dict.items():
        number_color_pairs = extract_number_color_pairs(value)
        max_line = calculate_max_line(number_color_pairs)

        if is_valid_game(max_line, max_counts):
            valid_game_ids.append(key)

        game_power_max = calculate_game_power(max_line)
        total_max_power += game_power_max

print("Number of valid games:", sum(map(int,valid_game_ids)))
print("Total power of maximum sets:", total_max_power)
