with open("2022/2022-12-02-input.txt", "r") as file:
    content = file.read()


def calculate_score_shape(game_list):
    """
    Scissors, paper, rock
    Score per shape selected
    """
    score = []

    for game in game_list:
        # shape selected
        if game[1] == "A":
            print(game, ": rock as 1")
            score.append(1)
        elif game[1] == "B":
            print(game, ": paper as 2")
            score.append(2)
        elif game[1] == "C":
            print(game, ": scissors as 3")
            score.append(3)
    return sum(score)


def calculate_score_result(game_list):
    """
    Scissors, paper, rock
    Score per result
    """
    win = [["A", "B"], ["B", "C"], ["C", "A"]]
    loss = [["B", "A"], ["C", "B"], ["A", "C"]]
    draw = [["A", "A"], ["B", "B"], ["C", "C"]]
    score = []

    for game in game_list:
        if game in draw:
            score.append(3)
            print(game, ": draw as 3")
        elif game in win:
            print(game, ": win as 6")
            score.append(6)
        elif game in loss:
            print(game, ": loss as 0")
            score.append(0)
    return sum(score)


def find_xyz(game_list):
    """
    Scissors, paper, rock
    X means you need to lose
    Y means you need to end the round in a draw
    Z means you need to win
    """
    for game in game_list:
        if game[1] == "Z":
            if game[0] == "A":
                game[1] = "B"
            elif game[0] == "B":
                game[1] = "C"
            elif game[0] == "C":
                game[1] = "A"
        elif game[1] == "Y":
            if game[0] == "A":
                game[1] = "A"
            elif game[0] == "B":
                game[1] = "B"
            elif game[0] == "C":
                game[1] = "C"
        elif game[1] == "X":
            if game[0] == "A":
                game[1] = "C"
            elif game[0] == "B":
                game[1] = "A"
            elif game[0] == "C":
                game[1] = "B"
    return game_list


# scenario one
content_1 = content.replace("X", "A").replace("Y", "B").replace("Z", "C")
games_1 = [line.split(" ") for line in content_1.strip().split("\n")]
print(calculate_score_shape(games_1) + calculate_score_result(games_1))

# scenario two
games_2 = [line.split(" ") for line in content.strip().split("\n")]
games_2 = find_xyz(games_2)
print(calculate_score_shape(games_2) + calculate_score_result(games_2))