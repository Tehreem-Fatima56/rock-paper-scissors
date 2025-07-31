import random

def play(player1, player2, num_games, verbose=False):
    p1 = ""
    p2 = ""
    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1 = player1(p2)
        p2 = player2(p1)

        if verbose:
            print(f"Player 1: {p1}  Player 2: {p2}")

        if p1 == p2:
            pass
        elif (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):
            p1_score += 1
        else:
            p2_score += 1

    if verbose:
        print(f"Final Score: Player 1: {p1_score}  Player 2: {p2_score}")

    return (p1_score, p2_score)


# Opponent Bots
def quincy(prev_play):
    sequence = ["R", "P", "P", "S", "R"]
    if prev_play == "":
        return "R"
    return sequence[(sequence.index(prev_play) + 1) % len(sequence)]

def abbey(prev_play):
    if prev_play == "":
        return "P"
    return {"R": "P", "P": "S", "S": "R"}[prev_play]

def kris(prev_play):
    if prev_play == "":
        return "S"
    return prev_play

def mr_x(prev_play):
    return random.choice(["R", "P", "S"])
