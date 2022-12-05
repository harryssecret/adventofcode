def read_strategy_data() -> list:
    rounds = []
    with open("strategy-data.txt") as f:
        elf_shape = ""
        my_shape = ""
        for line in f:
            for pos_char in range(len(line)):
                char = line[pos_char]
                if char == " ":
                    elf_shape = line[pos_char - 1]
                    my_shape = line[pos_char + 1]
                    rounds.append((elf_shape, my_shape))
    return rounds

# première colonne est ce que l'adversaire va jouer
# a is for rock
# b is for paper
# c is for scissors


# seconde colonne : c'est ce que je dois jouer X Y Z
shape_scores = {"rock": 1, "paper": 2, "scissors": 3}
outcome_score = {"lost": 0, "draw": 3, "won": 6}

wins_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
loose_against = {v: k for k, v in wins_against.items()}
# si adversaire = à notre coup alors tie
# sinon défaite


def compute_score(rounds: list) -> int:
    total_score = 0
    for game_round in rounds:
        elf_shape = getShapeName(game_round[0])
        my_shape = guess_shape_to_choose(elf_shape, game_round[1])

        round_status = who_won_fight(
            elf_shape, my_shape)

        total_score += shape_scores.get(my_shape) + \
            outcome_score.get(round_status)
    return total_score


def getShapeName(shape_code):
    if shape_code == "A":
        return "rock"
    elif shape_code == "B":
        return "paper"
    elif shape_code == "C":
        return "scissors"

# cependant gagner à chaque tour c'est de la triche
# part 2 need to guess shape to choose


def guess_shape_to_choose(elf_shape, should_i_win) -> str:
    if should_i_win == "Y":  # draw
        return elf_shape
    elif should_i_win == "X":  # loose
        return wins_against.get(elf_shape)
    elif should_i_win == "Z":  # win
        return loose_against.get(elf_shape)


def who_won_fight(elf_shape: str, my_shape: str) -> str:
    if elf_shape == my_shape:
        return 'draw'
    if wins_against.get(elf_shape) == my_shape:
        return 'lost'
    return 'won'


rounds = read_strategy_data()

final_score = compute_score(rounds)

print(final_score)
