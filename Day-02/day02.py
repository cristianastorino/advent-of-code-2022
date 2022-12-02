code_to_move = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS"
}

outcomes = {
    "ROCK": {
        "ROCK": "DRAW",
        "PAPER": "WIN",
        "SCISSORS": "LOSS"
    },
    "PAPER": {
        "ROCK": "LOSS",
        "PAPER": "DRAW",
        "SCISSORS": "WIN"
    },
    "SCISSORS": {
        "ROCK": "WIN",
        "PAPER": "LOSS",
        "SCISSORS": "DRAW"
    }
}

move_to_scores = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

round_to_scores = {
    "LOSS": 0,
    "DRAW": 3,
    "WIN": 6
}

def calc_round(line: str) -> int:
    opponent_move = code_to_move[line[0]]
    my_move = code_to_move[line[2]]
    round_outcome = outcomes[opponent_move][my_move]
    return move_to_scores[my_move] + round_to_scores[round_outcome]    

def calc_score(input: str) -> int:
    with open(input) as f:
        return sum(calc_round(line) for line in f)

score_small = calc_score("day02-small.txt")
assert score_small == 15

print(f"Part 1:\t{calc_score('day02.txt')}")

code_to_outcome = {
    "X": "LOSS",
    "Y": "DRAW",
    "Z": "WIN"
}

def calc_round_with_strategy(line: str) -> int:
    opponent_move = code_to_move[line[0]]
    round_outcome = code_to_outcome[line[2]]
    my_move = next(shape for shape in outcomes[opponent_move] if outcomes[opponent_move][shape] == round_outcome)
    return move_to_scores[my_move] + round_to_scores[round_outcome]

def calc_score_with_strategy(input: str) -> int:
    with open(input) as f:
        return sum(calc_round_with_strategy(line) for line in f)

score_small_part2 = calc_score_with_strategy("day02-small.txt")
assert score_small_part2 == 12

print(f"Part 2:\t{calc_score_with_strategy('day02.txt')}")