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
# si adversaire = à notre coup alors tie
# sinon défaite


def compute_score(rounds: list) -> int:
    total_score = 0
    for game_round in rounds:
        elf_shape = getShapeName(game_round[0])
        my_shape = getShapeName(game_round[1])

        round_status = who_won_fight(
            elf_shape, my_shape)

        total_score += shape_scores[my_shape] + outcome_score[round_status]
    return total_score


def getShapeName(shape_code):
    if shape_code == "A" or shape_code == "X":
        return "rock"
    elif shape_code == "B" or shape_code == "Y":
        return "paper"
    elif shape_code == "C" or shape_code == "Z":
        return "scissors"


def who_won_fight(elf_shape: str, my_shape: str) -> str:
    if elf_shape == my_shape:
        return 'draw'
    if wins_against[elf_shape] == my_shape:
        return 'lost'
    return 'won'


rounds = read_strategy_data()

final_score = compute_score(rounds)

print(final_score)
