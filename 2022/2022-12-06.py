with open("2022/2022-12-06-input.txt", "r") as file:
    stream = file.read().strip()


def find_index(n):
    """Find start of marker, with n unique values in string"""
    for s in range(len(stream) - 1):
        s1 = stream[s : s + n]
        if len(s1) == n & len(s1) == len(set(s1)):
            return s + n


print(find_index(4))
print(find_index(14))
